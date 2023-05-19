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

        return {"message": "order successful", "data": parcel_order.serialize()}, 201


class GetAllParcels(Resource):
    def get(self):
        """ method get all parcel orders"""
        return {"orders": [order.serialize() for order in parcels]}, 200


class GetSpecificParcelOrder(Resource):

    def get(self, parcel_id):
        """ Get a specific order"""
        parcel = Parcel().get_parcel_by_id(parcel_id)
        if parcel:
            return{"parcel": parcel.serialize()}, 200
        return {"message": "parcel not found"}


class CancelParcel(Resource):

    def put(self, parcel_id):
        parcel = Parcel().get_parcel_by_id(parcel_id)
        if parcel:
            if parcel.status == "cancelled":
                return {"message": "parcel already cancelled"}
            parcel.status == "cancelled"
            return {"message": "parcel order cancelled"}, 200
        return {"message": "order not found"}, 400


class GetUserParcels(Resource):
    '''Get user parcel orders '''

    def get(self, user_id):
        return{"userParcels": [order.serialize() for order in parcels if order.user_id == user_id]}, 200
