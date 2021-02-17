import requests
from app import create_app
import unittest
import json


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_get_city(self):
        """Test if return the correct city"""

        response = self.client.get('http://localhost:5000/weather/london')

        data = json.loads(response.data)

        result = "London"

        assert data['City_name'] == result

    def test_get_all_cities(self):
        """ Test if return the correct response quantity
        with different max queries """

        self.client.get('http://localhost:5000/weather/london')
        self.client.get('http://localhost:5000/weather/paris')
        self.client.get('http://localhost:5000/weather/porto')

        response = self.client.get('http://localhost:5000/weather?max=5')

        data = json.loads(response.data)
        assert len(data) == 3

        response = self.client.get('http://localhost:5000/weather?max=3')
        data = json.loads(response.data)
        assert len(data) == 3

        response = self.client.get('http://localhost:5000/weather?max=1')
        data = json.loads(response.data)
        assert len(data) == 1

        """ Test if after 6 requests, only 5 will be shown """

        self.client.get('http://localhost:5000/weather/berlin')
        self.client.get('http://localhost:5000/weather/curitiba')
        self.client.get('http://localhost:5000/weather/fortaleza')

        response = self.client.get('http://localhost:5000/weather?max=5')
        data = json.loads(response.data)
        assert len(data) == 5

        """ Test if the last request is the first item """

        assert data[0]['City_name'] == 'Fortaleza'


class FlaskTestViews(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_get_city(self):
        """ Test if endpoint is working """

        response = self.client.get('http://localhost:5000/weather/london')
        assert response.status_code == 200

    def test_get_all_city(self):
        """ Test if endpoint is working """

        response = self.client.get('http://localhost:5000/weather?max=1')
        assert response.status_code == 200
