from views import get_all_snakes, get_single_species, get_all_species, get_all_owners, get_single_owner, get_single_snake, create_snake, get_snakes_by_species


def all(resource):
    """For GET requests to collection"""
    if resource == "snakes":
        return get_all_snakes()
    elif resource == "owners":
        return get_all_owners()
    elif resource == "species":
        return get_all_species()
    else:
        return ''


def single(resource, id):
    """For GET requests to single resource"""
    response = None
    if resource == 'snakes':
        response = get_single_snake(id)
    elif resource == 'species':
        response = get_single_species(id)
    elif resource == 'owners':
        response = get_single_owner(id)
    else:
        response = ''
    return response


def query_get(query, resource):
    response = None
    if query.get('species') and resource == 'snakes':
        response = get_snakes_by_species(query['species'][0])
    return response


def get_all_or_single(self, resource, id):
    # check and make sure a valid resource comes through before running
    if id is not None:
        response = single(resource, id)
        if response is not None:
            response = response
        else:
            response = ''
    else:
        response = all(resource)
    return response


def create(resource, new_item):
    if resource == 'snakes':
        if 'name' in new_item and 'owner_id' in new_item and 'species_id' in new_item and 'gender' in new_item and 'color' in new_item:
            response = create_snake(new_item)
        else:
            response = {
                    "message": f'{" name is required" if "name" not in new_item else ""} {" owner_id is required" if "owner_id" not in new_item else ""}{" species_id is required" if "species_id" not in new_item else ""}{" gender is required" if "gender" not in new_item else ""}{" color is required" if "color" not in new_item else ""}'
                }
    else:
        response = ''
    return response


def delete(resource, id):
    """For DELETE requests"""
    response = ''
    return response


def update(resource, id, new_item):
    """For PUT requests"""
