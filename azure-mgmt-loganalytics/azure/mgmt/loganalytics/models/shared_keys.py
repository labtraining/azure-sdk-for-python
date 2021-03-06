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

from msrest.serialization import Model


class SharedKeys(Model):
    """The shared keys for a workspace.

    :param primary_shared_key: The primary shared key of a workspace.
    :type primary_shared_key: str
    :param secondary_shared_key: The secondary shared key of a workspace.
    :type secondary_shared_key: str
    """

    _attribute_map = {
        'primary_shared_key': {'key': 'primarySharedKey', 'type': 'str'},
        'secondary_shared_key': {'key': 'secondarySharedKey', 'type': 'str'},
    }

    def __init__(self, primary_shared_key=None, secondary_shared_key=None):
        self.primary_shared_key = primary_shared_key
        self.secondary_shared_key = secondary_shared_key
