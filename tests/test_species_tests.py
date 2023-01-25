import requests



def test_get_all_species():
    """
    Ensure we can get (GET) all species.
    """
    # Initiate GET request and capture the response
    response = requests.get('http://localhost:8088/species')

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
def test_get_single_species():
    """
    Ensure we can get (GET) a single species.
    """
    # Initiate GET request and capture the response
    response = requests.get('http://localhost:8088/species/1')
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
