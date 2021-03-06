# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401


import json

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Door(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None):  # noqa: E501
        """Door - a model defined in Swagger

        :param name: The name of this Door.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'name': str,
            'state': str
        }

        self.attribute_map = {
            'name': 'name',
            'state': 'state'
        }
        self._name = name
        self._state = 'close'

    def __repr__(self):
        door = {'name': self.name,
                'state': self.state}
        return json.dumps(door)

    @classmethod
    def from_dict(cls, dikt) -> 'Door':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Door of this Door.  # noqa: E501
        :rtype: Door
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Door.


        :return: The name of this Door.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Door.


        :param name: The name of this Door.
        :type name: str
        """

        self._name = name

    @property
    def state(self) -> str:
        """Gets the name of this Door.


        :return: The name of this Door.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the name of this Door.


        :param name: The name of this Door.
        :type name: str
        """

        self._state = state
