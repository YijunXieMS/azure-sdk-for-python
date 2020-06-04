# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CertificateBodyDescription
    from ._models_py3 import CertificateDescription
    from ._models_py3 import CertificateListDescription
    from ._models_py3 import CertificateProperties
    from ._models_py3 import CertificatePropertiesWithNonce
    from ._models_py3 import CertificateVerificationDescription
    from ._models_py3 import CertificateWithNonceDescription
    from ._models_py3 import CloudToDeviceProperties
    from ._models_py3 import EndpointHealthData
    from ._models_py3 import EnrichmentProperties
    from ._models_py3 import ErrorDetails, ErrorDetailsException
    from ._models_py3 import EventHubConsumerGroupInfo
    from ._models_py3 import EventHubProperties
    from ._models_py3 import ExportDevicesRequest
    from ._models_py3 import FailoverInput
    from ._models_py3 import FallbackRouteProperties
    from ._models_py3 import FeedbackProperties
    from ._models_py3 import GroupIdInformation
    from ._models_py3 import GroupIdInformationProperties
    from ._models_py3 import ImportDevicesRequest
    from ._models_py3 import IotHubCapacity
    from ._models_py3 import IotHubDescription
    from ._models_py3 import IotHubLocationDescription
    from ._models_py3 import IotHubNameAvailabilityInfo
    from ._models_py3 import IotHubProperties
    from ._models_py3 import IotHubQuotaMetricInfo
    from ._models_py3 import IotHubSkuDescription
    from ._models_py3 import IotHubSkuInfo
    from ._models_py3 import IpFilterRule
    from ._models_py3 import JobResponse
    from ._models_py3 import MatchedRoute
    from ._models_py3 import MessagingEndpointProperties
    from ._models_py3 import Name
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationInputs
    from ._models_py3 import PrivateEndpoint
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointConnectionProperties
    from ._models_py3 import PrivateLinkResources
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import RegistryStatistics
    from ._models_py3 import Resource
    from ._models_py3 import RouteCompilationError
    from ._models_py3 import RouteErrorPosition
    from ._models_py3 import RouteErrorRange
    from ._models_py3 import RouteProperties
    from ._models_py3 import RoutingEndpoints
    from ._models_py3 import RoutingEventHubProperties
    from ._models_py3 import RoutingMessage
    from ._models_py3 import RoutingProperties
    from ._models_py3 import RoutingServiceBusQueueEndpointProperties
    from ._models_py3 import RoutingServiceBusTopicEndpointProperties
    from ._models_py3 import RoutingStorageContainerProperties
    from ._models_py3 import RoutingTwin
    from ._models_py3 import RoutingTwinProperties
    from ._models_py3 import SharedAccessSignatureAuthorizationRule
    from ._models_py3 import StorageEndpointProperties
    from ._models_py3 import TagsResource
    from ._models_py3 import TestAllRoutesInput
    from ._models_py3 import TestAllRoutesResult
    from ._models_py3 import TestRouteInput
    from ._models_py3 import TestRouteResult
    from ._models_py3 import TestRouteResultDetails
    from ._models_py3 import UserSubscriptionQuota
    from ._models_py3 import UserSubscriptionQuotaListResult
except (SyntaxError, ImportError):
    from ._models import CertificateBodyDescription
    from ._models import CertificateDescription
    from ._models import CertificateListDescription
    from ._models import CertificateProperties
    from ._models import CertificatePropertiesWithNonce
    from ._models import CertificateVerificationDescription
    from ._models import CertificateWithNonceDescription
    from ._models import CloudToDeviceProperties
    from ._models import EndpointHealthData
    from ._models import EnrichmentProperties
    from ._models import ErrorDetails, ErrorDetailsException
    from ._models import EventHubConsumerGroupInfo
    from ._models import EventHubProperties
    from ._models import ExportDevicesRequest
    from ._models import FailoverInput
    from ._models import FallbackRouteProperties
    from ._models import FeedbackProperties
    from ._models import GroupIdInformation
    from ._models import GroupIdInformationProperties
    from ._models import ImportDevicesRequest
    from ._models import IotHubCapacity
    from ._models import IotHubDescription
    from ._models import IotHubLocationDescription
    from ._models import IotHubNameAvailabilityInfo
    from ._models import IotHubProperties
    from ._models import IotHubQuotaMetricInfo
    from ._models import IotHubSkuDescription
    from ._models import IotHubSkuInfo
    from ._models import IpFilterRule
    from ._models import JobResponse
    from ._models import MatchedRoute
    from ._models import MessagingEndpointProperties
    from ._models import Name
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import OperationInputs
    from ._models import PrivateEndpoint
    from ._models import PrivateEndpointConnection
    from ._models import PrivateEndpointConnectionProperties
    from ._models import PrivateLinkResources
    from ._models import PrivateLinkServiceConnectionState
    from ._models import RegistryStatistics
    from ._models import Resource
    from ._models import RouteCompilationError
    from ._models import RouteErrorPosition
    from ._models import RouteErrorRange
    from ._models import RouteProperties
    from ._models import RoutingEndpoints
    from ._models import RoutingEventHubProperties
    from ._models import RoutingMessage
    from ._models import RoutingProperties
    from ._models import RoutingServiceBusQueueEndpointProperties
    from ._models import RoutingServiceBusTopicEndpointProperties
    from ._models import RoutingStorageContainerProperties
    from ._models import RoutingTwin
    from ._models import RoutingTwinProperties
    from ._models import SharedAccessSignatureAuthorizationRule
    from ._models import StorageEndpointProperties
    from ._models import TagsResource
    from ._models import TestAllRoutesInput
    from ._models import TestAllRoutesResult
    from ._models import TestRouteInput
    from ._models import TestRouteResult
    from ._models import TestRouteResultDetails
    from ._models import UserSubscriptionQuota
    from ._models import UserSubscriptionQuotaListResult
from ._paged_models import EndpointHealthDataPaged
from ._paged_models import EventHubConsumerGroupInfoPaged
from ._paged_models import IotHubDescriptionPaged
from ._paged_models import IotHubQuotaMetricInfoPaged
from ._paged_models import IotHubSkuDescriptionPaged
from ._paged_models import JobResponsePaged
from ._paged_models import OperationPaged
from ._paged_models import SharedAccessSignatureAuthorizationRulePaged
from ._iot_hub_client_enums import (
    AccessRights,
    PublicNetworkAccess,
    IpFilterActionType,
    PrivateLinkServiceConnectionStatus,
    AuthenticationType,
    RoutingSource,
    Capabilities,
    IotHubReplicaRoleType,
    IotHubSku,
    IotHubSkuTier,
    EndpointHealthStatus,
    JobType,
    JobStatus,
    IotHubScaleType,
    IotHubNameUnavailabilityReason,
    TestResultStatus,
    RouteErrorSeverity,
)

__all__ = [
    'CertificateBodyDescription',
    'CertificateDescription',
    'CertificateListDescription',
    'CertificateProperties',
    'CertificatePropertiesWithNonce',
    'CertificateVerificationDescription',
    'CertificateWithNonceDescription',
    'CloudToDeviceProperties',
    'EndpointHealthData',
    'EnrichmentProperties',
    'ErrorDetails', 'ErrorDetailsException',
    'EventHubConsumerGroupInfo',
    'EventHubProperties',
    'ExportDevicesRequest',
    'FailoverInput',
    'FallbackRouteProperties',
    'FeedbackProperties',
    'GroupIdInformation',
    'GroupIdInformationProperties',
    'ImportDevicesRequest',
    'IotHubCapacity',
    'IotHubDescription',
    'IotHubLocationDescription',
    'IotHubNameAvailabilityInfo',
    'IotHubProperties',
    'IotHubQuotaMetricInfo',
    'IotHubSkuDescription',
    'IotHubSkuInfo',
    'IpFilterRule',
    'JobResponse',
    'MatchedRoute',
    'MessagingEndpointProperties',
    'Name',
    'Operation',
    'OperationDisplay',
    'OperationInputs',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionProperties',
    'PrivateLinkResources',
    'PrivateLinkServiceConnectionState',
    'RegistryStatistics',
    'Resource',
    'RouteCompilationError',
    'RouteErrorPosition',
    'RouteErrorRange',
    'RouteProperties',
    'RoutingEndpoints',
    'RoutingEventHubProperties',
    'RoutingMessage',
    'RoutingProperties',
    'RoutingServiceBusQueueEndpointProperties',
    'RoutingServiceBusTopicEndpointProperties',
    'RoutingStorageContainerProperties',
    'RoutingTwin',
    'RoutingTwinProperties',
    'SharedAccessSignatureAuthorizationRule',
    'StorageEndpointProperties',
    'TagsResource',
    'TestAllRoutesInput',
    'TestAllRoutesResult',
    'TestRouteInput',
    'TestRouteResult',
    'TestRouteResultDetails',
    'UserSubscriptionQuota',
    'UserSubscriptionQuotaListResult',
    'OperationPaged',
    'IotHubDescriptionPaged',
    'IotHubSkuDescriptionPaged',
    'EventHubConsumerGroupInfoPaged',
    'JobResponsePaged',
    'IotHubQuotaMetricInfoPaged',
    'EndpointHealthDataPaged',
    'SharedAccessSignatureAuthorizationRulePaged',
    'AccessRights',
    'PublicNetworkAccess',
    'IpFilterActionType',
    'PrivateLinkServiceConnectionStatus',
    'AuthenticationType',
    'RoutingSource',
    'Capabilities',
    'IotHubReplicaRoleType',
    'IotHubSku',
    'IotHubSkuTier',
    'EndpointHealthStatus',
    'JobType',
    'JobStatus',
    'IotHubScaleType',
    'IotHubNameUnavailabilityReason',
    'TestResultStatus',
    'RouteErrorSeverity',
]
