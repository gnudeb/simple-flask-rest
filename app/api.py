from flask import request, Response
from flask_restful import Api, Resource
from app import app
from app import models
import json
from json.decoder import JSONDecodeError
from jsonschema.exceptions import ValidationError

api = Api(app)
api_root = "/api"

class UserRegistration(Resource):

    def post(self):
        response = Response(mimetype="application/json")
        raw_json = request.form["data"]

        try:
            user = models.User.from_json(raw_json)
        except models.User.UserAlreadyExistsError:
            response.status = "409"
            response.data = json.dumps({
                "code": "USER_ALREADY_EXISTS",
                "description": "A user with specified username already exists"
            })
        except JSONDecodeError:
            response.status = "400"
            response.data = json.dumps({
                "code": "INVALID_JSON",
                "description": "Provided JSON is invalid"
            })
        except ValidationError:
            response.status = "400"
            response.data = json.dumps({
                "code": "INVALID_JSON_DATA",
                "description": "Provided JSON does not contain required data"
            })
        else:
            response.status = "200"
            response.data = user.to_json()
            models.User.create_user(user)

        return response



api.add_resource(UserRegistration, api_root+"/user")
