import sqlite3
import json
from models import Owner

SNAKES = []


def get_all_owners():
    """_gets all snakes from database_
    Returns:
        _type_: _list_
    """    ""
    # Open a connection to the database
    with sqlite3.connect("./snakes.sqlite3") as conn:
        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.first_name,
            a.last_name,
            a.email
        FROM Owners a
        """)
        # Initialize an empty list to hold all animal representations
        owners = []
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        # Iterate list of data returned from database
        for row in dataset:
            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            owner = Owner(row['id'], row['first_name'], row['last_name'],
                                row['email'])
            owners.append(owner.__dict__)
    return owners


def get_single_owner(id):
    """_summary_
    Args:
        id (_int_): _gets one snake by id_
    Returns:
        _type_: _dict_
    """
    with sqlite3.connect("./snakes.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.first_name,
            a.last_name,
            a.email
        FROM Owners a
        WHERE a.id = ?
        """, (id, ))
        # Load the single result into memory
        data = db_cursor.fetchone()
        # Create an animal instance from the current row
        owner = Owner(data['id'], data['first_name'], data['last_name'],
                            data['email'])
        return owner.__dict__


