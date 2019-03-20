from django.test import TestCase, Client
from rest_framework.test import force_authenticate, APIRequestFactory
from django.urls import reverse

import json

from users.models import User
from users.views import UsersList


class TestProfile(TestCase):
    """ class to test the user models """

    def setUp(self):
        """ dummy data to be used by the unit tests """
        self.username = 'susan'
        self.first_name = 'sue'
        self.last_name = 'nasimiyu'
        self.email = 'ronovalerie@gmail.com'
        self.password = '123abcxyz'

        self.updated_username = 'Eric'

        self.data = {
            "username" : self.username,
            "password" : self.password,
            "first_name" : self.first_name, 
            "last_name" : self.last_name,
            "email" : self.email
        }

        self.admin_data = {
            "username" : "Vinnyu",
            "password" : "Vinny",
            "first_name" : "Vincent", 
            "last_name" : "Odhiambo",
            "email" : "vodhiambo@gmail.com"
        }

        self.user = User(**self.data)

        self.admin = User(**self.admin_data)

        self.admin.is_staff=True
        self.admin.save()
        

        self.log_in_data = {
            "username" : self.username,
            "password" : self.password
        }

        self.updated_data = {
            "username" : "ericana",
            "password" : "Vinny"
        }
        
        self.client = Client()
        self.factory = APIRequestFactory()

    def tearDown(self):
        pass

    def test_user_registration(self):
        """ test whether a user can register to the system """

        response =  self.client.post(
            "/users/", data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_user_log_in(self):
        """ log in function """

        self.test_user_registration()
        response = self.client.post(
            "/api-token-auth/", data=json.dumps(self.log_in_data), content_type='application/json')
        token = response.json()['token']
        self.assertEqual(response.status_code, 200)
        return token

    def test_admin_can_view_all_users(self):
        """ test whether admin can view all users """

        view = UsersList.as_view()
        request = self.factory.get('/admin/users/')
        force_authenticate(request, user=self.admin)

        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_only_admin_can_delete_users(self):
        """ test whether regular user can delete users """

        token = self.test_user_log_in()
        headers = {'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.delete(
            "/users/1/", **headers, content_type='application/json')

        self.assertEqual(response.status_code, 403)
    

    def test_retrieve_non_existing_profile(self):
        """ test whether app catches non-existing user error """

        token = self.test_user_log_in()
        headers = {'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.get(
            "/users/200/", **headers, content_type='application/json')

        self.assertEqual(response.status_code, 404)

    def test_list_all_users_unauthorised(self):
        """ test whether app returns all available users with an unauthorised request """

        token = self.test_user_log_in()
        headers = {'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.get(
            "/users/", **headers, content_type='application/json')
        self.assertEqual(response.status_code, 403)

    