import sqlite3
import json
from models import Species

SNAKES = []


def get_all_species():
    """_gets all species from database_
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
            a.name
        FROM Species a
        """)
        # Initialize an empty list to hold all animal representations
        species = []
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        # Iterate list of data returned from database
        for row in dataset:
            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            snake = Species(row['id'], row['name'])
            species.append(snake.__dict__)
    return species


def get_single_species(id):
    """_summary_
    Args:
        id (_int_): _gets one species by id_
    Returns:
        _type_: _dict_
    """
    with sqlite3.connect("./snakes.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name
        FROM Species a
        WHERE a.id = ?
        """, (id, ))
        # Load the single result into memory
        data = db_cursor.fetchone()
        # Create an animal instance from the current row
        species = Species(data['id'], data['name'])
        return species.__dict__
