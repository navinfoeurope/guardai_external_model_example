# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from external_server.models.dataset_structure import DatasetStructure  # noqa: E501
from external_server.test import BaseTestCase


class TestDatasetController(BaseTestCase):
    """DatasetController integration test stubs"""

    def test_dataset_structure(self):
        """Test case for dataset_structure

        Get the dataset output structure
        """
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open("/dataset/structure", method="GET", headers=headers)
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_item(self):
        """Test case for get_item

        Get a dataset item
        """
        headers = {
            "Accept": "application/octet-stream",
        }
        response = self.client.open("/dataset/item/{item_idx}".format(item_idx=56), method="GET", headers=headers)
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
