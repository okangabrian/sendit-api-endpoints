from unittest import TestCase
import json
from app import create_app


class TestApp(TestCase):
    """ Setting up for testing """

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        '''tear down after testing'''
        self.app_context.pop()

    def test_signup(self):
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

    def test_login(self):
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

    def create_delivery(self):
        parcel_data = {
            "price": 500,
            "name": "brian",
            "pickup_location": "Westlands",
            "destination": "Karen",
            "weight": "3",
            "parcel_id": "Parcel.parcel_id_counter",
            "status": "pending"
        }

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

    def test_get_parcels(self):
        parcel_data = {
            "name": "microwave",
            "pickup_location": "juja",
            "destination": "voi",
            "price": 450,
            "weight": "2"
        }
        response = self.client.get(
            '/parcels',
            data=json.dumps(parcel_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 200)

    def test_get_specific_parcels(self, parcelId):
        parcel_data = {
            "name": "microwave",
            "pickup_location": "juja",
            "destination": "voi",
            "price": 450,
            "weight": "2"
        }
        response = self.client.get(
            '/parcel',
            data=json.dumps(parcel_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)[
                         'message'], "destination is invalid")

    def test_cancel_parcel(self, parcelId):
        parcel_data = {
            "name": "microwave",
            "pickup_location": "juja",
            "destination": "voi",
            "price": 450,
            "weight": "2"
        }
        response = self.client.put(
            '/parcel',
            data=json.dumps(parcel_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 200)

    def test_specific_user_parcels(self, parcelId):
        parcel_data = {
            "name": "microwave",
            "pickup_location": "juja",
            "destination": "voi",
            "price": 450,
            "weight": "2"
        }
        response = self.client.put(
            '/parcel',
            data=json.dumps(parcel_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 200)
