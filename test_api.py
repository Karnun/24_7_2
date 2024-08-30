import pytest
import requests
from api import PetFriends

@pytest.fixture
def get_api_key():
    res = requests.post("https://petfriends.skillfactory.ru/api/key", json={"email": "email@example.com", "password": "password"})
    return res.json()["key"]

def test_get_list_of_pets_with_valid_key(get_api_key):
    pet_friends = PetFriends(get_api_key)
    status_code, response = pet_friends.get_list_of_pets()
    assert status_code == 200
    assert 'pets' in response

def test_get_list_of_pets_with_invalid_key():
    pet_friends = PetFriends('invalid_key')
    status_code, response = pet_friends.get_list_of_pets()
    assert status_code == 403

def test_add_pet_without_name(get_api_key):
    pet_friends = PetFriends(get_api_key)
    status_code, response = pet_friends.add_pet('', 'dog', '3')
    assert status_code == 400

def test_add_pet_with_invalid_age(get_api_key):
    pet_friends = PetFriends(get_api_key)
    status_code, response = pet_friends.add_pet('Buddy', 'dog', 'invalid_age')
    assert status_code == 400

def test_delete_nonexistent_pet(get_api_key):
    pet_friends = PetFriends(get_api_key)
    status_code, response = pet_friends.delete_pet('invalid_id')
    assert status_code == 404

def test_update_pet_info_with_empty_data(get_api_key):
    pet_friends = PetFriends(get_api_key)
    status_code, response = pet_friends.update_pet_info('valid_pet_id', '', '', '')
    assert status_code == 400

def test_get_pet_info_with_valid_id(get_api_key):
    pet_friends = PetFriends(get_api_key)
    status_code, response = pet_friends.get_pet_info('valid_pet_id')
    assert status_code == 200
    assert 'name' in response
    assert 'animal_type' in response
    assert 'age' in response

def test_add_pet_with_photo(get_api_key):
    pet_friends = PetFriends(get_api_key)
    with open('path/to/photo.jpg', 'rb') as photo:
        status_code, response = pet_friends.add_pet('Fluffy', 'cat', '2', pet_photo=photo)
    assert status_code == 200
    assert 'id' in response

def test_get_list_of_pets_with_filter(get_api_key):
    pet_friends = PetFriends(get_api_key)
    status_code, response = pet_friends.get_list_of_pets(filter='my_filter')
    assert status_code == 200
    assert 'pets' in response

def test_add_new_pet_without_photo(get_api_key):
    pet_friends = PetFriends(get_api_key)
    status_code, response = pet_friends.add_new_pet_without_photo('Sparky', 'dog', '4')
    assert status_code == 200
    assert 'id' in response
