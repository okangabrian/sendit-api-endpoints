from ..models.models import Parcel, User, users, parcels
from flask_restful import Resource, reqparse


class PostParcel(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=int, required=True)
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("ordered_by", type=int, required=True)
    parser.add_argument("pickup_location", type=str, required=True)
    parser.add_argument("destination", type=str, required=True)
    parser.add_argument("weight", type=int, required=True)

    def post(self):
        """ method create parcel order """
        data = PostParcel.parser.parse_args()
        price = data["price"]
        name = data["name"]
        order_by = data["ordered_by"]
        pickup_location = data["pickup_location"]
        destination = data["destination"]
        weight = data["weight"]

        parcel_order = Parcel(price, name, order_by,
                              pickup_location, destination, weight)
        parcels.append(parcel_order)

        print(parcel_order.orderd_by)

        return {"message": "order successful"}, 201


class Get_all_Parcels(Resource):
    def get(self):
        """ method get all parcel orders"""
        return {"orders": [order.serialize() for order in parcels]}

    # class Get_specific_order(Resource):
    #     def get_specific_order(self)
    #     """ method specific parcel order by id"""
