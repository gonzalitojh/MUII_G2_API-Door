# coding: utf-8

from __future__ import absolute_import

from unittest import mock

from flask import json

from swagger_server.models.door import Door  # noqa: E501
from swagger_server.models.update_door import UpdateDoor  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDoorController(BaseTestCase):
    """DoorController integration test stubs"""

    @mock.patch("muii_g2_family_lock_database.Database.PostgresDB.add_new_door")
    def test_add_door(self, mocked_add_new_door):
        """Test case for add_door

        Add a new door to the system
        """
        body = Door()
        mocked_add_new_door.assert_not_called()
        mocked_add_new_door.return_value = None
        response = self.client.open(
            '/door',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        mocked_add_new_door.assert_called_once()
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @mock.patch("muii_g2_family_lock_database.Database.PostgresDB.delete_door")
    def test_delete_door(self, mocked_delete_door):
        """Test case for delete_door

        Delete a door
        """
        mocked_delete_door.assert_not_called()
        mocked_delete_door.return_value = None
        response = self.client.open(
            '/door/{id}'.format(id=56),
            method='DELETE')
        mocked_delete_door.assert_called_once()
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @mock.patch("muii_g2_family_lock_database.Database.PostgresDB.get_all_doors_state")
    def test_get_all_doors_state(self, mocked_get_all_doors_state):
        """Test case for get_all_doors_state

        Get all doors state
        """
        mocked_get_all_doors_state.assert_not_called()
        mocked_get_all_doors_state.return_value = [
            [
                "Living room door",
                3,
                "open"
            ],
            [
                "Main door",
                1,
                "close"
            ]
        ]
        response = self.client.open(
            '/door',
            method='GET')
        mocked_get_all_doors_state.assert_called_once()
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @mock.patch("muii_g2_family_lock_database.Database.PostgresDB.get_door_state")
    def test_get_door_state(self, mocked_get_door_state):
        """Test case for get_door_state

        Get a door state
        """
        mocked_get_door_state.assert_not_called()
        mocked_get_door_state.return_value = [
            [
                "Living room door",
                3,
                "open"
            ]
        ]

        response = self.client.open(
            '/door/{id}'.format(id=56),
            method='GET')
        mocked_get_door_state.assert_called_once()
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @mock.patch("muii_g2_family_lock_database.Database.PostgresDB.update_door_state")
    def test_update_door_state(self, mocked_update_door_state):
        """Test case for update_door_state

        Update door state
        """
        mocked_update_door_state.assert_not_called()
        mocked_update_door_state.return_value = None
        body = UpdateDoor()
        response = self.client.open(
            '/door',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        mocked_update_door_state.assert_called_once()
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
