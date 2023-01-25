import sqlite3
import json
from models import Snake

SNAKES = []


def get_all_snakes():
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
            a.name,
            a.owner_id,
            a.species_id,
            a.gender,
            a.color
        FROM Snakes a
        """)
        # Initialize an empty list to hold all animal representations
        snakes = []
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        # Iterate list of data returned from database
        for row in dataset:
            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            snake = Snake(row['id'], row['name'], row['owner_id'],
                        row['species_id'], row['gender'], row['color'])
            snakes.append(snake.__dict__)
    return snakes


def get_single_snake(id):
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
            a.name,
            a.owner_id,
            a.species_id,
            a.gender,
            a.color
        FROM Snakes a
        WHERE a.id = ?
        """, (id, ))
        # Load the single result into memory
        data = db_cursor.fetchone()
        # Create an animal instance from the current row
        snake = Snake(data['id'], data['name'], data['owner_id'],
                    data['species_id'], data['gender'], data['color'])
        if 'species_id' in snake.__dict__ and snake.__dict__['species_id'] == 2:
            return {}
        else:
            return snake.__dict__


def create_snake(new_snake):
    with sqlite3.connect("./snakes.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Snakes
            ( name, owner_id, species_id, gender, color )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_snake['name'], new_snake['owner_id'],
              new_snake['species_id'], new_snake['gender'],
              new_snake['color'], ))
        id = db_cursor.lastrowid
        new_snake['id'] = id
        conn.commit()
        return new_snake


def get_snakes_by_species(species_id):
    with sqlite3.connect("./snakes.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.owner_id,
            a.species_id,
            a.gender,
            a.color
        FROM Snakes a
        WHERE a.species_id = ?
        """, (species_id, ))
        snakes = []
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        # Iterate list of data returned from database
        for row in dataset:
            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            snake = Snake(row['id'], row['name'], row['owner_id'],
                        row['species_id'], row['gender'], row['color'])
            snakes.append(snake.__dict__)
    return snakes
