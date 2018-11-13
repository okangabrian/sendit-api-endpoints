from ..models.models import Parcel, User, users, parcels
from flask_restful import Resource, reqparse

from flask_jwt_extended import jwt_required, get_jwt_identity


class PostParcel(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=int, required=True)
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("pickup_location", type=str, required=True)
    parser.add_argument("destination", type=str, required=True)
    parser.add_argument("weight", type=int, required=True)

    @jwt_required
    def post(self):
        """ method create parcel order """
        data = PostParcel.parser.parse_args()
        price = data["price"]
        name = data["name"]
        pickup_location = data["pickup_location"]
        destination = data["destination"]
        weight = data["weight"]

        user = get_jwt_identity()

        parcel_order = Parcel(price, name, user,
                              pickup_location, destination, weight)
        parcels.append(parcel_order)

        return {"message": "order successful"}, 201


class Get_all_Parcels(Resource):
    def get(self):
        """ method get all parcel orders"""
        return {"orders": [order.serialize() for order in parcels]}, 200


class Get_specific_parcel_order(Resource):
    def get(self, parcel_id):
        """ method specific parcel order by id"""

        parcel = Parcel().get_parcel_by_id(parcel_id)

        if not parcel:
            return {"message": "parcel not found"}, 404
        return{"message": parcel.serialize()}, 200
