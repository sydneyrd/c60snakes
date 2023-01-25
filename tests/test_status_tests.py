import requests

def test_unsupported_get():
    """
    Ensure an unsupported endpoint returns a blank request body and status code 404.
    """
    # Initiate GET request to an unsupported endpoint
    response = requests.get('http://localhost:8088/unsupported')
    # Assert that the response status code is 404
    assert response.status_code == 404
    # Assert that the response body is blank
    # assert isinstance(response.json, str)
    assert response.json() == ""

def test_unsupported_post():
    """
    Ensure an unsupported endpoint returns a blank request body and status code 404.
    """
    # Initiate POST request to an unsupported endpoint
    snake = {
	"name":"adminsnake",
	"owner_id": 1,
	"species_id": 1,
	"gender": "female",
	"color": "blue"
    }
    response = requests.post('http://localhost:8088/unsupported', json='snake')
    # Assert that the response status code is 404
    assert response.status_code == 404
    # Assert that the response body is blank
    # assert isinstance(response.json, str)
    assert response.json() == ""
    # assert response.text == ""


def test_unsupported_put():
    """
    Ensure an unsupported endpoint returns a blank request body and status code 404.
    """
    # Initiate PUT request to an unsupported endpoint
    response = requests.put('http://localhost:8088/unsupported/1')
    # Assert that the response status code is 404
    assert response.status_code == 404
    # Assert that the response body is blank
    # assert response.json() == ""
    assert isinstance(response.json(), str)
    assert response.json() == ""
    
def test_unsupported_delete():
    """
    Ensure an unsupported endpoint returns a blank request body and status code 404.
    """
    # Initiate DELETE request to an unsupported endpoint
    response = requests.delete('http://localhost:8088/unsupported/1')

    # Assert that the response status code is 404
    assert response.status_code == 404
    # Assert that the response body is blank
    assert isinstance(response.json(), str)
    assert response.json() == ""