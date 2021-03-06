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


class RecognizedEntityGroup(Model):
    """Defines a group of previously recognized entities.

    :param recognized_entity_regions: The regions of the image that contain
     entities.
    :type recognized_entity_regions:
     list[~azure.cognitiveservices.search.imagesearch.models.RecognizedEntityRegion]
    :param name: The name of the group where images of the entity were also
     found. The following are possible groups. CelebRecognitionAnnotations:
     Similar to CelebrityAnnotations but provides a higher probability of an
     accurate match. CelebrityAnnotations: Contains celebrities such as actors,
     politicians, athletes, and historical figures.
    :type name: str
    """

    _validation = {
        'recognized_entity_regions': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'recognized_entity_regions': {'key': 'recognizedEntityRegions', 'type': '[RecognizedEntityRegion]'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, recognized_entity_regions, name):
        self.recognized_entity_regions = recognized_entity_regions
        self.name = name
