from django.test import TestCase, Client
from django.urls import reverse

import json
# Create your tests here.
from users.models import User


class TestProfile(TestCase):
    """ class to test the user models """

    def setUp(self):
        """ dummy data to be used by the unit tests """
        self.username = 'susan'
        self.first_name = 'sue'
        self.last_name = 'nasimiyu'
        self.email = 'ronovalerie@gmail.com'
        self.password = '123abcxyz'

        # create a user that will be logged in
        self.user_one = User(
            self.username, self.first_name,
            self.last_name, self.email,
            self.password)

        self.data = {
            "username" : self.username,
            "password" : self.password
        }

        self.data1 = {
            "username" : self.username,
            "email" : self.email,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "password" : self.password
        }

        self.updated_data = {
            "username" : "ericana",
            "password" : self.password
        }
        
        self.client = Client()

    def tearDown(self):
        pass

    def log_in_user(self):
        """ log in function """
        self.register_user()
        response = self.client.post(
            "/api-token-auth/", data=json.dumps(self.data), content_type='application/json')
        token = response.json()['token']
        return token
    
    def register_user(self):
        """ Register a new user to the system """
        return self.client.post(
            "/users/", data=json.dumps(self.data1), content_type='application/json')

    def test_retrieve_non_existing_profile(self):
        """ test whether app catches non-existing user error """
        token = self.log_in_user()
        headers = {'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.get(
            "/users/200/", **headers, content_type='application/json')

        self.assertEqual(response.status_code, 404)

    def test_list_all_users_unauthorised(self):
        """ test whether app returns all available users with an unauthorised request"""
        token = self.log_in_user()
        headers = {'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.get(
            "/users/", **headers, content_type='application/json')
        self.assertEqual(response.status_code, 403)

    # 
        