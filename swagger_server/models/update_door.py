# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UpdateDoor(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, name: str=None, state: str=None):  # noqa: E501
        """UpdateDoor - a model defined in Swagger

        :param id: The id of this UpdateDoor.  # noqa: E501
        :type id: int
        :param state: The state of this UpdateDoor.  # noqa: E501
        :type state: str
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'state': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'state': 'state'
        }
        self._id = id
        self._name = name
        self._state = state

    @classmethod
    def from_dict(cls, dikt) -> 'UpdateDoor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpdateDoor of this UpdateDoor.  # noqa: E501
        :rtype: UpdateDoor
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this UpdateDoor.


        :return: The id of this UpdateDoor.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this UpdateDoor.


        :param id: The id of this UpdateDoor.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the id of this UpdateDoor.


        :return: The id of this UpdateDoor.
        :rtype: int
        """
        return self._name

    @id.setter
    def name(self, name: str):
        """Sets the id of this UpdateDoor.


        :param id: The id of this UpdateDoor.
        :type id: int
        """

        self._name = name

    @property
    def state(self) -> str:
        """Gets the state of this UpdateDoor.


        :return: The state of this UpdateDoor.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this UpdateDoor.


        :param state: The state of this UpdateDoor.
        :type state: str
        """

        self._state = state
