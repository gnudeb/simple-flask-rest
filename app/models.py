from flask_sqlalchemy import SQLAlchemy
from app import app
import json
import jsonschema

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.String(16), primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    user_name = db.Column(db.String(64))
    plain_password = db.Column(db.String(64))
    hashed_password = db.Column(db.String(128))

    json_schema = {
            "type": "object",
            "properties": {
                "firstName": {"type": "string"},
                "lastName": {"type": "string"},
                "userName": {"type": "string"},
                "password": {"type": "string"},
            },
            "required": [
                "firstName",
                "lastName",
                "userName",
                "password",
            ],
    }

    def __init__(self, first_name, last_name, user_name, plain_password):
        if User.exists(user_name):
            raise User.UserAlreadyExistsError

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.plain_password = plain_password
        self.id = len(User.query.all())

    def exists(user_name):
        return User.query.filter_by(user_name=user_name).first() is not None

    def from_json(raw_json):
        data = json.loads(raw_json)
        jsonschema.validate(data, User.json_schema)
        
        user = User(
                first_name=data["firstName"],
                last_name=data["lastName"],
                user_name=data["userName"],
                plain_password=data["password"]
        )

        return user

    def create_user(user):
        db.session.add(user)
        db.session.commit()

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {
                "id": self.id,
                "firstName": self.first_name,
                "lastName": self.last_name,
                "userName": self.user_name
        }


    class UserAlreadyExistsError(Exception):
        pass

    def __repr__(self):
        return "<User {}>".format(self.id)
