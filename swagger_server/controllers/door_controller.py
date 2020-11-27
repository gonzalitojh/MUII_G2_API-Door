import connexion
import six

from swagger_server.models.door import Door  # noqa: E501
from swagger_server.models.update_door import UpdateDoor  # noqa: E501
from swagger_server import util

import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
DATABASE_HOST = os.environ['DATABASE_HOST']
DATABASE_USER = os.environ['DATABASE_USER']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASE_NAME = os.environ['DATABASE_NAME']


def add_door(door):  # noqa: E501
    """Add a new door to the system

    Add a new door to the system # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        door = Door.from_dict(connexion.request.get_json())  # noqa: E501

    connection = psycopg2.connect(user=DATABASE_USER,
                                  password=DATABASE_PASSWORD,
                                  host=DATABASE_HOST,
                                  port="5432",
                                  database=DATABASE_NAME)
    cursor = connection.cursor()

    try:
        postgres_insert_query = '''INSERT INTO door (name) VALUES (%s)'''
        cursor.execute(postgres_insert_query, (door.name,))

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        if connection:
            print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    return "Door inserted successfully"


def delete_door(door_id):  # noqa: E501
    """Delete a door

    Delete a door # noqa: E501

    :param door_id: ID of door
    :type door_id: int

    :rtype: str
    """

    connection = psycopg2.connect(user=DATABASE_USER,
                                  password=DATABASE_PASSWORD,
                                  host=DATABASE_HOST,
                                  port="5432",
                                  database=DATABASE_NAME)
    cursor = connection.cursor()

    try:
        # Update single record now
        sql_delete_query = """DELETE FROM door WHERE id = %s"""
        cursor.execute(sql_delete_query, (door_id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    return 'Door deleted successfully'


def get_all_doors_state():  # noqa: E501
    """Get all doors state

    Get all doors state # noqa: E501


    :rtype: str
    """

    connection = psycopg2.connect(user=DATABASE_USER,
                                  password=DATABASE_PASSWORD,
                                  host=DATABASE_HOST,
                                  port="5432",
                                  database=DATABASE_NAME)
    cursor = connection.cursor()

    try:
        sql_select_query = """SELECT * FROM door"""
        cursor.execute(sql_select_query)
        record = cursor.fetchall()

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    return record


def get_door_state(door_id):  # noqa: E501
    """Get a door state

    Get a door state # noqa: E501

    :param door_id: ID of door
    :type door_id: int

    :rtype: str
    """

    connection = psycopg2.connect(user=DATABASE_USER,
                                  password=DATABASE_PASSWORD,
                                  host=DATABASE_HOST,
                                  port="5432",
                                  database=DATABASE_NAME)
    cursor = connection.cursor()

    try:
        sql_select_query = """SELECT * FROM door WHERE id = %s"""
        cursor.execute(sql_select_query, (door_id,))
        record = cursor.fetchall()

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    return record


def update_door_state(door):  # noqa: E501
    """Update door state

    Update door state # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    print('##################################')
    print(connexion.request.get_json())
    print('##################################')
    if connexion.request.is_json:
        door = UpdateDoor.from_dict(connexion.request.get_json())  # noqa: E501
    print('##################################')
    print(door)
    print('##################################')

    connection = psycopg2.connect(user=DATABASE_USER,
                                  password=DATABASE_PASSWORD,
                                  host=DATABASE_HOST,
                                  port="5432",
                                  database=DATABASE_NAME)
    cursor = connection.cursor()

    try:
        # Update single record now
        sql_update_query = """UPDATE door SET state = %s WHERE name = %s"""
        cursor.execute(sql_update_query, (door.state, door.name))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    return 'Door updated successfully'
