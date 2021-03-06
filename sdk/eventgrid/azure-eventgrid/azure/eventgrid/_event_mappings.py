# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from ._generated import models

_event_mappings = {
    "Microsoft.AppConfiguration.KeyValueDeleted": models.AppConfigurationKeyValueDeletedEventData,
    "Microsoft.AppConfiguration.KeyValueModified": models.AppConfigurationKeyValueModifiedEventData,
    "Microsoft.ContainerRegistry.ImagePushed": models.ContainerRegistryImagePushedEventData,
    "Microsoft.ContainerRegistry.ImageDeleted": models.ContainerRegistryImageDeletedEventData,
    "Microsoft.ContainerRegistry.ChartDeleted": models.ContainerRegistryChartDeletedEventData,
    "Microsoft.ContainerRegistry.ChartPushed": models.ContainerRegistryChartPushedEventData,
    "Microsoft.Devices.DeviceCreated": models.IotHubDeviceCreatedEventData,
    "Microsoft.Devices.DeviceDeleted": models.IotHubDeviceDeletedEventData,
    "Microsoft.Devices.DeviceConnected": models.IotHubDeviceConnectedEventData,
    "Microsoft.Devices.DeviceDisconnected": models.IotHubDeviceDisconnectedEventData,
    "Microsoft.Devices.DeviceTelemetry": models.IotHubDeviceTelemetryEventData,
    "Microsoft.EventGrid.SubscriptionValidationEvent": models.SubscriptionValidationEventData,
    "Microsoft.EventGrid.SubscriptionDeletedEvent": models.SubscriptionDeletedEventData,
    "Microsoft.EventHub.CaptureFileCreated": models.EventHubCaptureFileCreatedEventData,
    "Microsoft.MachineLearningServices.DatasetDriftDetected": models.MachineLearningServicesDatasetDriftDetectedEventData,
    "Microsoft.MachineLearningServices.ModelDeployed": models.MachineLearningServicesModelDeployedEventData,
    "Microsoft.MachineLearningServices.ModelRegistered": models.MachineLearningServicesModelRegisteredEventData,
    "Microsoft.MachineLearningServices.RunCompleted": models.MachineLearningServicesRunCompletedEventData,
    "Microsoft.MachineLearningServices.RunStatusChanged": models.MachineLearningServicesRunStatusChangedEventData,
    "Microsoft.Maps.GeofenceEntered": models.MapsGeofenceEnteredEventData,
    "Microsoft.Maps.GeofenceExited": models.MapsGeofenceExitedEventData,
    "Microsoft.Maps.GeofenceResult": models.MapsGeofenceResultEventData,
    "Microsoft.Media.JobStateChange": models.MediaJobStateChangeEventData,
    "Microsoft.Media.JobOutputStateChange": models.MediaJobOutputStateChangeEventData,
    "Microsoft.Media.JobScheduled": models.MediaJobScheduledEventData,
    "Microsoft.Media.JobProcessing": models.MediaJobProcessingEventData,
    "Microsoft.Media.JobCanceling": models.MediaJobCancelingEventData,
    "Microsoft.Media.JobFinished": models.MediaJobFinishedEventData,
    "Microsoft.Media.JobCanceled": models.MediaJobCanceledEventData,
    "Microsoft.Media.JobErrored": models.MediaJobErroredEventData,
    "Microsoft.Media.JobOutputCanceled": models.MediaJobOutputCanceledEventData,
    "Microsoft.Media.JobOutputCanceling": models.MediaJobOutputCancelingEventData,
    "Microsoft.Media.JobOutputErrored": models.MediaJobOutputErroredEventData,
    "Microsoft.Media.JobOutputFinished": models.MediaJobOutputFinishedEventData,
    "Microsoft.Media.JobOutputProcessing": models.MediaJobOutputProcessingEventData,
    "Microsoft.Media.JobOutputScheduled": models.MediaJobOutputScheduledEventData,
    "Microsoft.Media.JobOutputProgress": models.MediaJobOutputProgressEventData,
    "Microsoft.Media.LiveEventEncoderConnected": models.MediaLiveEventEncoderConnectedEventData,
    "Microsoft.Media.LiveEventConnectionRejected": models.MediaLiveEventConnectionRejectedEventData,
    "Microsoft.Media.LiveEventEncoderDisconnected": models.MediaLiveEventEncoderDisconnectedEventData,
    "Microsoft.Media.LiveEventIncomingStreamReceived": models.MediaLiveEventIncomingStreamReceivedEventData,
    "Microsoft.Media.LiveEventIncomingStreamsOutOfSync": models.MediaLiveEventIncomingStreamsOutOfSyncEventData,
    "Microsoft.Media.LiveEventIncomingVideoStreamsOutOfSync": models.MediaLiveEventIncomingVideoStreamsOutOfSyncEventData,
    "Microsoft.Media.LiveEventIncomingDataChunkDropped": models.MediaLiveEventIncomingDataChunkDroppedEventData,
    "Microsoft.Media.LiveEventIngestHeartbeat": models.MediaLiveEventIngestHeartbeatEventData,
    "Microsoft.Media.LiveEventTrackDiscontinuityDetected": models.MediaLiveEventTrackDiscontinuityDetectedEventData,
    "Microsoft.Resources.ResourceWriteSuccess": models.ResourceWriteSuccessData,
    "Microsoft.Resources.ResourceWriteFailure": models.ResourceWriteFailureData,
    "Microsoft.Resources.ResourceWriteCancel": models.ResourceWriteCancelData,
    "Microsoft.Resources.ResourceDeleteSuccess": models.ResourceDeleteSuccessData,
    "Microsoft.Resources.ResourceDeleteFailure": models.ResourceDeleteFailureData,
    "Microsoft.Resources.ResourceDeleteCancel": models.ResourceDeleteCancelData,
    "Microsoft.Resources.ResourceActionSuccess": models.ResourceActionSuccessData,
    "Microsoft.Resources.ResourceActionFailure": models.ResourceActionFailureData,
    "Microsoft.Resources.ResourceActionCancel": models.ResourceActionCancelData,
    "Microsoft.ServiceBus.ActiveMessagesAvailableWithNoListeners": models.ServiceBusActiveMessagesAvailableWithNoListenersEventData,
    "Microsoft.ServiceBus.DeadletterMessagesAvailableWithNoListener": models.ServiceBusDeadletterMessagesAvailableWithNoListenersEventData,
    "Microsoft.Storage.BlobCreated": models.StorageBlobCreatedEventData,
    "Microsoft.Storage.BlobDeleted": models.StorageBlobDeletedEventData,
    "Microsoft.Storage.BlobRenamed": models.StorageBlobRenamedEventData,
    "Microsoft.Storage.DirectoryCreated": models.StorageDirectoryCreatedEventData,
    "Microsoft.Storage.DirectoryDeleted": models.StorageDirectoryDeletedEventData,
    "Microsoft.Storage.DirectoryRenamed": models.StorageDirectoryRenamedEventData,
    "Microsoft.Storage.LifecyclePolicyCompleted": models.StorageLifecyclePolicyCompletedEventData,
    "Microsoft.Web.AppUpdated": models.WebAppUpdatedEventData,
    "Microsoft.Web.BackupOperationStarted": models.WebBackupOperationStartedEventData,
    "Microsoft.Web.BackupOperationCompleted": models.WebBackupOperationCompletedEventData,
    "Microsoft.Web.BackupOperationFailed": models.WebBackupOperationFailedEventData,
    "Microsoft.Web.RestoreOperationStarted": models.WebRestoreOperationStartedEventData,
    "Microsoft.Web.RestoreOperationCompleted": models.WebRestoreOperationCompletedEventData,
    "Microsoft.Web.RestoreOperationFailed": models.WebRestoreOperationFailedEventData,
    "Microsoft.Web.SlotSwapStarted": models.WebSlotSwapStartedEventData,
    "Microsoft.Web.SlotSwapCompleted": models.WebSlotSwapCompletedEventData,
    "Microsoft.Web.SlotSwapFailed": models.WebSlotSwapFailedEventData,
    "Microsoft.Web.SlotSwapWithPreviewStarted": models.WebSlotSwapWithPreviewStartedEventData,
    "Microsoft.Web.SlotSwapWithPreviewCancelled": models.WebSlotSwapWithPreviewCancelledEventData,
    "Microsoft.Web.AppServicePlanUpdated": models.WebAppServicePlanUpdatedEventData,
}