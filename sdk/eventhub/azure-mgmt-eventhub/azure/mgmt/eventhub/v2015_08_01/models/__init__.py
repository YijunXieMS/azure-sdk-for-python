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
    from ._models_py3 import CheckNameAvailabilityParameter
    from ._models_py3 import CheckNameAvailabilityResult
    from ._models_py3 import ConsumerGroupCreateOrUpdateParameters
    from ._models_py3 import ConsumerGroupResource
    from ._models_py3 import EventHubCreateOrUpdateParameters
    from ._models_py3 import EventHubResource
    from ._models_py3 import NamespaceCreateOrUpdateParameters
    from ._models_py3 import NamespaceResource
    from ._models_py3 import NamespaceUpdateParameter
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import RegenerateKeysParameters
    from ._models_py3 import Resource
    from ._models_py3 import ResourceListKeys
    from ._models_py3 import SharedAccessAuthorizationRuleCreateOrUpdateParameters
    from ._models_py3 import SharedAccessAuthorizationRuleResource
    from ._models_py3 import Sku
    from ._models_py3 import TrackedResource
except (SyntaxError, ImportError):
    from ._models import CheckNameAvailabilityParameter
    from ._models import CheckNameAvailabilityResult
    from ._models import ConsumerGroupCreateOrUpdateParameters
    from ._models import ConsumerGroupResource
    from ._models import EventHubCreateOrUpdateParameters
    from ._models import EventHubResource
    from ._models import NamespaceCreateOrUpdateParameters
    from ._models import NamespaceResource
    from ._models import NamespaceUpdateParameter
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import RegenerateKeysParameters
    from ._models import Resource
    from ._models import ResourceListKeys
    from ._models import SharedAccessAuthorizationRuleCreateOrUpdateParameters
    from ._models import SharedAccessAuthorizationRuleResource
    from ._models import Sku
    from ._models import TrackedResource
from ._paged_models import ConsumerGroupResourcePaged
from ._paged_models import EventHubResourcePaged
from ._paged_models import NamespaceResourcePaged
from ._paged_models import OperationPaged
from ._paged_models import SharedAccessAuthorizationRuleResourcePaged
from ._event_hub_management_client_enums import (
    SkuName,
    SkuTier,
    NamespaceState,
    AccessRights,
    Policykey,
    EntityStatus,
    UnavailableReason,
)

__all__ = [
    'CheckNameAvailabilityParameter',
    'CheckNameAvailabilityResult',
    'ConsumerGroupCreateOrUpdateParameters',
    'ConsumerGroupResource',
    'EventHubCreateOrUpdateParameters',
    'EventHubResource',
    'NamespaceCreateOrUpdateParameters',
    'NamespaceResource',
    'NamespaceUpdateParameter',
    'Operation',
    'OperationDisplay',
    'RegenerateKeysParameters',
    'Resource',
    'ResourceListKeys',
    'SharedAccessAuthorizationRuleCreateOrUpdateParameters',
    'SharedAccessAuthorizationRuleResource',
    'Sku',
    'TrackedResource',
    'OperationPaged',
    'NamespaceResourcePaged',
    'SharedAccessAuthorizationRuleResourcePaged',
    'EventHubResourcePaged',
    'ConsumerGroupResourcePaged',
    'SkuName',
    'SkuTier',
    'NamespaceState',
    'AccessRights',
    'Policykey',
    'EntityStatus',
    'UnavailableReason',
]