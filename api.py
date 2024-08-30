import requests

class PetFriends:
    def __init__(self, api_key=None):
        self.base_url = "https://petfriends.skillfactory.ru/"
        self.api_key = api_key

    def get_api_key(self, email, password):
       
        headers = {'Content-Type': 'application/json'}
        data = {'email': email, 'password': password}
        res = requests.post(self.base_url + 'api/key', headers=headers, json=data)
        return res.status_code, res.json()

    def get_list_of_pets(self, filter=None):

        headers = {'auth_key': self.api_key}
        params = {'filter': filter} if filter else {}
        res = requests.get(self.base_url + 'api/pets', headers=headers, params=params)
        return res.status_code, res.json()

    def add_pet(self, name, animal_type, age, pet_photo=None):

        headers = {'auth_key': self.api_key}
        data = {'name': name, 'animal_type': animal_type, 'age': age}
        files = {'pet_photo': open(pet_photo, 'rb')} if pet_photo else {}
        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data, files=files)
        return res.status_code, res.json()

    def delete_pet(self, pet_id):

        headers = {'auth_key': self.api_key}
        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        return res.status_code, res.json()

    def update_pet_info(self, pet_id, name, animal_type, age):

        headers = {'auth_key': self.api_key}
        data = {'name': name, 'animal_type': animal_type, 'age': age}
        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        return res.status_code, res.json()

    def add_new_pet_without_photo(self, name, animal_type, age):

        return self.add_pet(name, animal_type, age)

    def add_pet_photo(self, pet_id, pet_photo):

        headers = {'auth_key': self.api_key}
        files = {'pet_photo': open(pet_photo, 'rb')}
        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, files=files)
        return res.status_code, res.json()

    def get_pet_info(self, pet_id):

        headers = {'auth_key': self.api_key}
        res = requests.get(self.base_url + 'api/pets/' + pet_id, headers=headers)
        return res.status_code, res.json()
