#!/usr/bin/env python3
import unittest
from app import app
from app.models import db, User
from flask_migrate import Migrate
import json
from json import JSONDecodeError
from jsonschema.exceptions import ValidationError

class CRUDTestSuite(unittest.TestCase):

    user_dummy = {
            "first_name": "John",
            "last_name": "Cleese",
            "user_name": "lancelot",
            "plain_password": "knightswhosayni",
            }


    user_dummy_json = json.dumps({
            "firstName": "John",
            "lastName": "Cleese",
            "userName": "lancelot",
            "password": "knightswhosayni",
    })


    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        self.app = app.test_client()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def post(self, client_data):
        return self.app.post('/api/user', data=dict(data=client_data))


    def test_can_create_user_by_post_request(self):
        self.post(self.user_dummy_json)
        assert User.query.first().user_name == "lancelot"


    def test_successful_user_creation_returns_user_object(self):
        response = self.post(self.user_dummy_json)


    def test_username_collision_returns_an_error(self):
        self.post(self.user_dummy_json)
        response = self.post(self.user_dummy_json)

        assert response.status_code == 409

        # 'Response.data()' returns a bytearray, hense 'decode()'
        data = json.loads(response.data.decode())
        assert data["code"] == "USER_ALREADY_EXISTS"


    def test_invalid_json_returns_an_error(self):
        client_json = '{"user'
        response = self.post(client_json)
        data = json.loads(response.data.decode())
        assert data["code"] == "INVALID_JSON"

    def test_invalid_post_request_returns_an_error(self):
        client_json = json.dumps({
                "userName": "lancelot"
        })
        response = self.post(client_json)
        data = json.loads(response.data.decode())
        assert data["code"] == "INVALID_JSON_DATA"


if __name__ == "__main__":
    unittest.main()
