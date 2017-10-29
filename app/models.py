from flask_sqlalchemy import SQLAlchemy
from app import app
import json

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.String(16), primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    user_name = db.Column(db.String(64))
    plain_password = db.Column(db.String(64))
    hashed_password = db.Column(db.String(128))

    def exists(user_name):
        return User.query.filter_by(user_name=user_name).first() is not None

    def from_json(raw_json):
        data = json.loads(raw_json)
        if User.exists(data["userName"]):
            raise User.UserAlreadyExistsError

        user = User(
                id=len(User.query.all()),
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
        json_object = {
                "id": self.id,
                "firstName": self.first_name,
                "lastName": self.last_name,
                "userName": self.user_name
        }
        return json.dumps(json_object)

    class UserAlreadyExistsError(Exception):
        pass

    def __repr__(self):
        return "<User {}>".format(self.id)
