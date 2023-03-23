import json

import requests


class TestAuthorsAPI:
    url = "https://fakerestapi.azurewebsites.net"
    endpoint = '/api/v1/Authors'

    def test_get_authors(self):
        response = requests.get(self.url + self.endpoint)
        assert response.status_code == 200

    def test_create_author(self):
        host = self.url + self.endpoint
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            "id": 0,
            "idBook": 0,
            "firstName": "Test",
            "lastName": "Author"
        }
        response = requests.post(host, headers=headers, json=data)
        assert response.status_code == 200

    def test_update_user(self):
        author_id = 15
        endpoint = f'/api/v1/Authors/{author_id}'
        host = self.url + endpoint
        payload = {
            "id": author_id,
            "idBook": 2,
            "firstName": "updated",
            "lastName": "user"
        }
        response = requests.request("PUT", host, json=payload)
        assert response.status_code == 200

    def test_delete_user(self):
        author_id = 10
        endpoint = f'/api/v1/Authors/{author_id}'
        host = self.url + endpoint
        response = requests.request("DELETE", host)
        assert response.status_code == 200
