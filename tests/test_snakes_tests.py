import requests


def test_get_all_snakes():
    """
    Ensure we can get (GET) all species.
    """
    # Initiate GET request and capture the response
    response = requests.get('http://localhost:8088/snakes')

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_snakes():
    """
    Ensure we can create (POST) a new snake.
    """
    snake = {
	"name":"adminsnake",
	"owner_id": 1,
	"species_id": 1,
	"gender": "female",
	"color": "blue"
    }
    # Initiate POST request and capture the response
    response = requests.post('http://localhost:8088/snakes', json=snake)
    # Assert that the response status code is 201 (CREATED)
    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert response.json()['name'] == 'adminsnake'

def test_get_single_snake():
    """
    Ensure we can get (GET) a single snake.
    """
    # Initiate GET request and capture the response
    response = requests.get('http://localhost:8088/snakes/2')

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_snakes_by_species():
    """'
    Ensure we can get (GET) all snakes my their fk species id
    """
    species_id = 1
    response = requests.get(f'http://localhost:8088/snakes?species={species_id}')
    assert response.status_code == 200
    assert response.json()[0]['species_id'] == species_id
    assert isinstance(response.json(), list)

def test_post_incomplete_snake():
    """
    Ensure when sending an incomplete snake object, we get a 400 error
    """
    snake = {    
    "name":"adminsnake",
    "owner_id": 1}
    response = requests.post('http://localhost:8088/snakes', json=snake)
    assert response.status_code == 400
    assert 'color' in response.json()['message']

def test_no_alone_snakes():
    """_ make sure the aonyxx cinerea is not got alone :( _
    """
    response = requests.get('http://localhost:8088/snakes/1')
    assert response.status_code == 405
    