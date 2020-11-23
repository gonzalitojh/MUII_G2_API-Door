import connexion
import six

from swagger_server.models.door import Door  # noqa: E501
from swagger_server.models.update_door import UpdateDoor  # noqa: E501
from swagger_server import util


def add_door(visit):  # noqa: E501
    """Add a new door to the system

    Add a new door to the system # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Door.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_door(id):  # noqa: E501
    """Delete a door

    Delete a door # noqa: E501

    :param id: ID of door
    :type id: int

    :rtype: str
    """
    return 'do some magic!'


def get_all_doors_state():  # noqa: E501
    """Get all doors state

    Get all doors state # noqa: E501


    :rtype: str
    """
    return 'do some magic!'


def get_door_state(id):  # noqa: E501
    """Get a door state

    Get a door state # noqa: E501

    :param id: ID of door
    :type id: int

    :rtype: str
    """
    return 'do some magic!'


def update_door_state(visit):  # noqa: E501
    """Update door state

    Update door state # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = UpdateDoor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
