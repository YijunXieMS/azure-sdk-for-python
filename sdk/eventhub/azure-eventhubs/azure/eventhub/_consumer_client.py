# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import logging
from typing import Any, Union, TYPE_CHECKING
from ._common import EventPosition,\
    EventHubSharedKeyCredential, EventHubSASTokenCredential
from ._eventprocessor.event_processor import EventProcessor
from ._client import EventHubClient
if TYPE_CHECKING:
    from azure.core.credentials import TokenCredential  # type: ignore

log = logging.getLogger(__name__)


class EventHubConsumerClient(EventHubClient):
    """Represents an AMQP connection to an EventHub and receives event data from it.

    Example:
        .. code-block:: python

            import asyncio
            import logging
            import os
            from azure.eventhub.aio import EventHubConsumerClient
            from azure.eventhub.aio import FileBasedPartitionManager

            RECEIVE_TIMEOUT = 5  # timeout in seconds for a receiving operation. 0 or None means no timeout
            RETRY_TOTAL = 3  # max number of retries for receive operations within the receive timeout. Actual number of retries clould be less if RECEIVE_TIMEOUT is too small
            CONNECTION_STR = os.environ["EVENT_HUB_CONN_STR"]

            logging.basicConfig(level=logging.INFO)

            def process_events(partition_context, events):
                if events:
                    # do something
                    partition_context.update_checkpoint(events[-1])
                else:
                    print("empty events received", "partition:", partition_context.partition_id)


            if __name__ == '__main__':
                partition_manager = FileBasedPartitionManager("consumer_pm_store")
                client = EventHubConsumerClient.from_connection_string(
                    CONNECTION_STR, partition_manager=partition_manager, receive_timeout=RECEIVE_TIMEOUT, retry_total=RETRY_TOTAL
                )
    """

    def __init__(self, host, event_hub_path, credential, **kwargs):
        # type:(str, str, Union[EventHubSharedKeyCredential, EventHubSASTokenCredential, TokenCredential], Any) -> None
        """
        :param host: The hostname of the Event Hub.
        :type host: str
        :param event_hub_path: The path of the specific Event Hub to connect the client to.
        :type event_hub_path: str
        :param network_tracing: Whether to output network trace logs to the logger. Default
         is `False`.
        :type network_tracing: bool
        :param credential: The credential object used for authentication which implements particular interface
         of getting tokens. It accepts ~azure.eventhub.EventHubSharedKeyCredential,
         ~azure.eventhub.EventHubSASTokenCredential, credential objects generated by the azure-identity library and
         objects that implement get_token(self, *scopes) method.
        :param http_proxy: HTTP proxy settings. This must be a dictionary with the following
         keys: 'proxy_hostname' (str value) and 'proxy_port' (int value).
         Additionally the following keys may also be present: 'username', 'password'.
        :type http_proxy: dict[str, Any]
        :param auth_timeout: The time in seconds to wait for a token to be authorized by the service.
         The default value is 60 seconds. If set to 0, no timeout will be enforced from the client.
        :type auth_timeout: float
        :param user_agent: The user agent that needs to be appended to the built in user agent string.
        :type user_agent: str
        :param retry_total: The total number of attempts to redo the failed operation when an error happened. Default
         value is 3.
        :type retry_total: int
        :param transport_type: The type of transport protocol that will be used for communicating with
         the Event Hubs service. Default is ~azure.eventhub.TransportType.Amqp.
        :type transport_type: ~azure.eventhub.TransportType
        :param partition_manager: stores the load balancing data and checkpoint data when receiving events
         if partition_manager is specified. If it's None, this EventHubConsumerClient instance will receive
         events without load balancing and checkpointing.
        :type partition_manager: PartitionManager.
        :param load_balancing_interval: When load balancing kicks in, this is the interval in seconds
         between two load balancing. Default 10.
        :type load_balancing_interval: float
        """

        super(EventHubConsumerClient, self).__init__(host=host, event_hub_path=event_hub_path, credential=credential, **kwargs)
        self._partition_manager = kwargs.get("partition_manager")
        self._load_balancing_interval = kwargs.get("load_balancing_interval", 10)
        self._event_processors = dict()
        self._closed = False

    def _stop_eventprocessor(self, event_processor, consumer_group, partition_id):
        with self._lock:
            event_processor.stop()
            if partition_id and (consumer_group, partition_id) in self._event_processors:
                del self._event_processors[(consumer_group, partition_id)]
            elif (consumer_group, '-1') in self._event_processors:
                del self._event_processors[(consumer_group, "-1")]

    def receive(
            self, event_handler, consumer_group, *, partition_id=None,
            owner_level=None, prefetch=None, track_last_enqueued_event_properties=False,
            initial_event_position=None,
            error_handler=None, partition_initialize_handler=None, partition_close_handler=None,
    ):
        """Receive events from partition(s) optionally with load balancing and checkpointing.

        :param event_handler:
        :param consumer_group:
        :param partition_id:
        :param owner_level:
        :param prefetch:
        :param track_last_enqueued_event_properties:
        :param initial_event_position:
        :param error_handler:
        :param partition_initialize_handler:
        :param partition_close_handler:
        :return: None
        """
        with self._lock:
            error = None
            if (consumer_group, '-1') in self._event_processors:
                error = ValueError("This consumer client is already receiving events from all partitions for"
                                 " consumer group {}. "
                                 "Shouldn't receive from any other partitions again".format(consumer_group))
            elif partition_id is None and [x for x in self._event_processors.keys() if x[0] == consumer_group]:
                error = ValueError("This consumer client is already receiving events for consumer group {}. "
                                 "Shouldn't receive from all partitions again".format(consumer_group))
            elif (consumer_group, partition_id) in self._event_processors:
                error = ValueError("This consumer is already receiving events from partition {} for consumer group {}. "
                                 "Shouldn't receive from it again.".format(partition_id, consumer_group))
            if error:
                log.warning(error)
                raise error

            event_processor = EventProcessor(
                self, consumer_group, event_handler,
                partition_id=partition_id,
                partition_manager=self._partition_manager,
                error_handler=error_handler,
                partition_initialize_handler=partition_initialize_handler,
                partition_close_handler=partition_close_handler,
                initial_event_position=initial_event_position or EventPosition("-1"),
                polling_interval=self._load_balancing_interval,
                owner_level=owner_level,
                prefetch=prefetch,
                track_last_enqueued_event_properties=track_last_enqueued_event_properties,
            )
            if partition_id:
                self._event_processors[(consumer_group, partition_id)] = event_processor
            else:
                self._event_processors[(consumer_group, "-1")] = event_processor

            event_processor.start()
            return Task(self, event_processor)

    def get_last_enqueued_event_properties(self, consumer_group: str, partition_id: str):
        """The latest enqueued event information of a partition.
        This property will be updated each time an event is received when
        the client is created with `track_last_enqueued_event_properties` being `True`.
        The dict includes following information of the partition:

            * `sequence_number`
            * `offset`
            * `enqueued_time`
            * `retrieval_time`

        :rtype: dict or None
        :raises: ValueError
        """
        if (consumer_group, partition_id) in self._event_processors:
            return self._event_processors[(consumer_group, partition_id)].get_last_enqueued_event_properties(partition_id)
        elif (consumer_group, '-1') in self._event_processors:
            return self._event_processors[(consumer_group, -1)].get_last_enqueued_event_properties(
                partition_id)
        else:
            raise ValueError("You're not receiving events from partition {} for consumer group {}".
                             format(partition_id, consumer_group))

    def close(self):
        # type: () -> None
        """Stop retrieving events from event hubs and close the underlying AMQP connection and links.

        """
        with self._lock:
            for _ in range(len(self._event_processors)):
                _, ep = self._event_processors.popitem()
                ep.stop()
            super().close()


class Task:
    def __init__(self, consumer_client, event_processor):
        self._consumer_client = consumer_client
        self._event_processor = event_processor
        self._partition_id = event_processor._partition_id
        self._consumer_group_name = event_processor._consumer_group_name

    def cancel(self):
        self._consumer_client._stop_eventprocessor(self._event_processor, self._consumer_group_name, self._partition_id)
        log.info("Task of EventProcessor %r has been cancelled successfully.", self._event_processor._id)
