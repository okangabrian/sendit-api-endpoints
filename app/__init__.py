from .api.V1.views.user import PostUser

from .api.V1.views.parcels import PostParcel, Get_all_Parcels, Get_specific_parcel_order
from flask import Flask
from flask_restful import Api


def create_up():
    app = Flask(__name__)
    sendIt = Api(app)
    sendIt.add_resource(PostUser, '/auth/signup')
    sendIt.add_resource(PostParcel, '/parcel')
    sendIt.add_resource(Get_all_Parcels, '/parcels')
    sendIt.add_resource(Get_specific_parcel_order, '/parcels/<int:parcel_id>')

    return app
