import connexion
from flask import jsonify
from muii_g2_family_lock_database.Database import PostgresDB

from swagger_server.models.door import Door  # noqa: E501
from swagger_server.models.update_door import UpdateDoor  # noqa: E501


def add_door(door):  # noqa: E501
    """Add a new door to the system

    Add a new door to the system # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        door = Door.from_dict(connexion.request.get_json())  # noqa: E501

    db = PostgresDB()
    error = db.add_new_door(door.name)
    if error:
        return error
    return "Door inserted successfully"


def delete_door(door_id):  # noqa: E501
    """Delete a door

    Delete a door # noqa: E501

    :param door_id: ID of door
    :type door_id: int

    :rtype: str
    """
    db = PostgresDB()
    error = db.delete_door(door_id)
    if error:
        return error
    return 'Door deleted successfully'


def get_all_doors_state():  # noqa: E501
    """Get all doors state

    Get all doors state # noqa: E501


    :rtype: str
    """
    db = PostgresDB()
    doors = db.get_all_doors_state()
    if "Error" in doors:
        return doors

    return jsonify({"doors": doors})


def get_door_state(door_id):  # noqa: E501
    """Get a door state

    Get a door state # noqa: E501

    :param door_id: ID of door
    :type door_id: int

    :rtype: str
    """
    db = PostgresDB()
    door = db.get_door_state(door_id)
    if "Error" in door:
        return door
    return jsonify({"door": door})


def update_door_state(door):  # noqa: E501
    """Update door state

    Update door state # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        door = UpdateDoor.from_dict(connexion.request.get_json())  # noqa: E501

    db = PostgresDB()
    error = db.update_door_state(door.state, door.name)
    if error:
        return error
    return 'Door updated successfully'
