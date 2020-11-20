# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.door import Door  # noqa: E501
from swagger_server.models.update_door import UpdateDoor  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDoorController(BaseTestCase):
    """DoorController integration test stubs"""

    def test_add_door(self):
        """Test case for add_door

        Add a new door to the system
        """
        body = Door()
        response = self.client.open(
            '/door',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_door(self):
        """Test case for delete_door

        Delete a door
        """
        response = self.client.open(
            '/door/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_doors_state(self):
        """Test case for get_all_doors_state

        Get all doors state
        """
        response = self.client.open(
            '/door',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_door_state(self):
        """Test case for get_door_state

        Get a door state
        """
        response = self.client.open(
            '/door/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_door_state(self):
        """Test case for update_door_state

        Update door state
        """
        body = UpdateDoor()
        response = self.client.open(
            '/door',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
