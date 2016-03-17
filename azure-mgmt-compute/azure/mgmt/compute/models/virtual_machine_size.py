# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualMachineSize(Model):
    """
    Describes the properties of a VM size.

    :param str name: Gets or sets the VM size name.
    :param int number_of_cores: Gets or sets the Number of cores supported by
     a VM size.
    :param int os_disk_size_in_mb: Gets or sets the OS disk size allowed by a
     VM size.
    :param int resource_disk_size_in_mb: Gets or sets the Resource disk size
     allowed by a VM size.
    :param int memory_in_mb: Gets or sets the Memory size supported by a VM
     size.
    :param int max_data_disk_count: Gets or sets the Maximum number of data
     disks allowed by a VM size.
    """ 

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'number_of_cores': {'key': 'numberOfCores', 'type': 'int'},
        'os_disk_size_in_mb': {'key': 'osDiskSizeInMB', 'type': 'int'},
        'resource_disk_size_in_mb': {'key': 'resourceDiskSizeInMB', 'type': 'int'},
        'memory_in_mb': {'key': 'memoryInMB', 'type': 'int'},
        'max_data_disk_count': {'key': 'maxDataDiskCount', 'type': 'int'},
    }

    def __init__(self, name=None, number_of_cores=None, os_disk_size_in_mb=None, resource_disk_size_in_mb=None, memory_in_mb=None, max_data_disk_count=None, **kwargs):
        self.name = name
        self.number_of_cores = number_of_cores
        self.os_disk_size_in_mb = os_disk_size_in_mb
        self.resource_disk_size_in_mb = resource_disk_size_in_mb
        self.memory_in_mb = memory_in_mb
        self.max_data_disk_count = max_data_disk_count