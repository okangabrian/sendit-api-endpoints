from ..models.models import Parcel, User, users, parcels
from flask_restful import Resource, reqparse
from ..utils.validate import validate_username
from flask import Blueprint, render_template


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

        if not validate_username(self, name):
            return {"message": "enter a correct name format"}, 400

            if type(price) != int:
                return {"message": "please enter an interger"}, 400
            if type(weight) != int:
                return {"message": "enter a valid weight"}, 400

            parcel_order = Parcel(price, name, user,
                                  pickup_location, destination, weight)
            parcels.append(parcel_order)
            return parcel_order
            return {"message": "order successful"}, 201


class GetAllParcels(Resource):
    def get(self):
        """ method get all parcel orders"""
        return {"orders": [order.serialize() for order in parcels]}, 200


class GetSpecificParcelOrder(Resource):
    parser = reqparse.RequestParser()

    def get(self, parcel_id):
        """ Get a specific order"""
        parcel = Parcel().get_parcel_by_id(parcel_id)

        if not parcel:
            return {"message": "parcel not found"}, 404
        return{"message": parcel.serialize()}, 200


class CancelParcel(Resource):

    def put(self, parcel_id):
        parcel = Parcel().get_parcel_by_id(parcel_id)
        if parcel:
            if parcel.status == "cancelled":
                return {"message": "parcel already cancelled"}
            parcel.status == "cancelled"
            return {"message": "parcel order cancelled"}, 200
        return {"message": "order not found"}, 400


# class GetUserParcels(Resource):
#     '''Get parcel orders for specific users'''

#     def get(self, id):
#         for parcel in parcels:
