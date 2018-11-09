from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash

from ..models.models import Parcel, User, users, parcels


class PostUser(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True)
    parser.add_argument("password", type=str, required=True)

    def post(self):
        """ method create user """
        data = PostUser.parser.parse_args()
        username = data["username"]
        password = data["password"]
        user = User(username, password)
        users.append(user)
        return {"message": "successful"}, 201
