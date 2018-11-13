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


class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True)
    parser.add_argument("password", type=str, required=True)

    def post(self):
        data = Login.parser.parse_args()

        username = data["username"]
        password = data["password"]

        user = User().get_user_by_name(username)

        if not user:
            return {'message': 'user not found'}, 404

        if not check_password_hash(user.password, password):
            return {'message': 'incorrect password'}, 401
        return {"message": 'login successful'}
