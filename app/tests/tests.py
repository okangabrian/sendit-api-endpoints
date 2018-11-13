from unittest import TestCase
import json
from app import create_up


class TestApp(TestCase):
    """ Setting up for testing """

    def setUp(self):
        self.app = create_up()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        '''tear down after testing'''
        self.app_context.pop()

    def signup(self):
        signup_data = {
            "username": "brian",
            "password": "brian"
        }

        response = self.client.post(
            "/auth/signup",
            data=json.dumps(signup_data),
            headers={'content-type': 'application/json'}
        )
        return response

    def login(self):
        login_data = {
            "username": "brian",
            "password": "brian"
        }

        response = self.client.post(
            "/auth/login",
            data=json.dumps(login_data),
            headers={'content-type': 'application/json'}
        )
        return response

    def test_user_signup(self):

        response = self.signup()

        self.assertEqual(response.status_code, 201)

    def test_login(self):
        response = self.signup()

        res = self.login()
        self.assertEqual(res.status_code, 200)

    def test_create_parcel(self):
        parcel_data = {
            "name": "microwave",
            "pickup_location": "juja",
            "destination": "voi",
            "price": 450,
            "weight": "2"
        }
        response = self.client.post(
            '/parcel',
            data=json.dumps(parcel_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 201)
