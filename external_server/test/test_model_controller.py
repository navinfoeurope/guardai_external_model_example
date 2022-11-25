# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from external_server.models.model_structure import ModelStructure  # noqa: E501
from external_server.test import BaseTestCase


class TestModelController(BaseTestCase):
    """ModelController integration test stubs"""

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_predict(self):
        """Test case for predict

        Perform prediction on a model
        """
        headers = {
            "Accept": "application/octet-stream",
            "Content-Type": "multipart/form-data",
        }
        data = dict(data="/path/to/file", names=["names_example"])
        response = self.client.open(
            "/model", method="POST", headers=headers, data=data, content_type="multipart/form-data"
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_structure(self):
        """Test case for structure

        Get model input and output structures
        """
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open("/model", method="GET", headers=headers)
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
