# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from external_server.models.base_model_ import Model
from external_server.models.dataset_structure_features_inner import DatasetStructureFeaturesInner
from external_server import util

from external_server.models.dataset_structure_features_inner import DatasetStructureFeaturesInner  # noqa: E501


class DatasetStructure(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, num_items=None, features=None):  # noqa: E501
        """DatasetStructure - a model defined in OpenAPI

        :param num_items: The num_items of this DatasetStructure.  # noqa: E501
        :type num_items: int
        :param features: The features of this DatasetStructure.  # noqa: E501
        :type features: List[DatasetStructureFeaturesInner]
        """
        self.openapi_types = {"num_items": int, "features": List[DatasetStructureFeaturesInner]}

        self.attribute_map = {"num_items": "num_items", "features": "features"}

        self._num_items = num_items
        self._features = features

    @classmethod
    def from_dict(cls, dikt) -> "DatasetStructure":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DatasetStructure of this DatasetStructure.  # noqa: E501
        :rtype: DatasetStructure
        """
        return util.deserialize_model(dikt, cls)

    @property
    def num_items(self):
        """Gets the num_items of this DatasetStructure.


        :return: The num_items of this DatasetStructure.
        :rtype: int
        """
        return self._num_items

    @num_items.setter
    def num_items(self, num_items):
        """Sets the num_items of this DatasetStructure.


        :param num_items: The num_items of this DatasetStructure.
        :type num_items: int
        """

        self._num_items = num_items

    @property
    def features(self):
        """Gets the features of this DatasetStructure.


        :return: The features of this DatasetStructure.
        :rtype: List[DatasetStructureFeaturesInner]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this DatasetStructure.


        :param features: The features of this DatasetStructure.
        :type features: List[DatasetStructureFeaturesInner]
        """

        self._features = features