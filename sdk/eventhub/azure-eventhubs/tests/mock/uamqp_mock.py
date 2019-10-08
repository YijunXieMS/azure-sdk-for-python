import uamqp
import time
import datetime
from azure.eventhub import EventHubClient, EventPosition, EventData, EventHubSharedKeyCredential


def create_message(offset, sn):
    message = uamqp.Message(body="AAA")
    annotations = {}
    annotations[EventData.PROP_OFFSET] = offset
    annotations[EventData.PROP_SEQ_NUMBER] = sn
    annotations[EventData.PROP_TIMESTAMP] = datetime.datetime.now().timestamp() * 1000
    message.annotations = annotations
    return message




class Link(object):
    def __init__(self):
        self.peer_max_message_size = 256 * 1024


class MessageSender(object):
    def __init__(self):
        self._link = Link()


class MessageReceiver(object):
    def __init__(self):
        self._link = Link()


class AMQPClientMock(object):
    def __init__(
            self, remote_address, auth=None, client_name=None, debug=False,
            error_policy=None, keep_alive_interval=None, **kwargs):
        pass

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()

    def open(self, connection=None):
        pass

    def close(self):
        pass

    def mgmt_request(self, message, operation, op_type=None, node=None, callback=None, **kwargs):
        pass

    def auth_complete(self):
        return True

    def client_ready(self):
        return True

    def do_work(self):
        pass


from mock_eventhubs_sync import MessageStoreSync
message_store = MessageStoreSync(2)


class SendClientMock(AMQPClientMock):
    def __init__(
            self, target, auth=None, client_name=None, debug=False, msg_timeout=0,
            error_policy=None, keep_alive_interval=None, **kwargs):
        super(SendClientMock, self).__init__(
            target,
            auth=auth,
            client_name=client_name,
            debug=debug,
            error_policy=error_policy,
            keep_alive_interval=keep_alive_interval,
            **kwargs)
        self._msg_timeout = 0
        self._pending_messages = []
        self._waiting_messages = 0
        self._shutdown = None
        self.message_handler = MessageSender()
        self.partition = kwargs.get("partition", None)
        self.store = message_store

    def messages_pending(self):
        return bool(self._pending_messages)

    def queue_message(self, *messages):
        for message in messages:
            for internal_message in message.gather():
                internal_message.idle_time = time.perf_counter() * 1000  # milliseconds
                internal_message.state = uamqp.constants.MessageState.WaitingToBeSent
                self._pending_messages.append(internal_message)


    @property
    def pending_messages(self):
        return [m for m in self._pending_messages if m.state in uamqp.constants.PENDING_STATES]

    def wait(self):
        for message in self._pending_messages:
            if message.state in uamqp.constants.PENDING_STATES:
                message.state = uamqp.constants.MessageState.SendComplete
                message.on_send_complete(uamqp.constants.MessageSendResult.Ok, None)
                self.store.save_message(message, pid=self.partition)
        self._pending_messages = []
        return True


class ReceiveClientMock(AMQPClientMock):
    def __init__(
            self, source, auth=None, client_name=None, debug=False, timeout=0,
            auto_complete=True, error_policy=None, **kwargs):
        super(ReceiveClientMock, self).__init__(
            source, auth=auth, client_name=client_name, error_policy=error_policy, debug=debug, **kwargs)
        self.message_handler = MessageReceiver()
        self.partition = int(str(source).split('/')[-1])
        self.store = message_store

    def receive_message_batch(self, max_batch_size=None, on_message_received=None, timeout=0):
        if not max_batch_size:
            max_batch_size = 300
        if not timeout:
            timeout = 1000
        return self.store.retrieve_messages(self.partition, max_batch_size, timeout)

    def receive_messages_iter(self, on_message_received=None):
        while True:
            yield self.store.retrieve_messages(self.partition, size=1, timeout=0)


def create_auth():
    return None


client = EventHubClient("host", "name", EventHubSharedKeyCredential("", ""))
client._create_auth = create_auth

producer = client.create_producer(partition_id="0")
producer._send_client_type = SendClientMock

'''
batch = producer.create_batch()
batch.try_add(EventData("AAA"))
batch.try_add(EventData("BBB"))
producer.send(batch)
'''
producer.send(EventData("AAA"))
producer.send(EventData("AAA"))
producer.send(EventData("AAA"))
producer.send(EventData("AAA"))


consumer = client.create_consumer("consumer_group", "0", EventPosition("-1"))
consumer._receive_client_type = ReceiveClientMock

events = consumer.receive(timeout=2)
for item in events:
    print(item)
