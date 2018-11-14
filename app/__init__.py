from flask_restful import Api
from flask import Flask
from .api.V1.views.user import PostUser, Login

from app.api.V1.views.parcels import PostParcel
from app.api.V1.views.parcels import GetSpecificParcelOrder
from app.api.V1.views.parcels import GetAllParcels
from app.api.V1.views.parcels import CancelParcel


def create_app():
    app = Flask(__name__)
    app.secret_key = "hgsgluglsgurwltteiuwtlaiw"
    sendIt.add_resource(PostUser, '/auth/signup')
    sendIt.add_resource(PostParcel, '/parcel')
    sendIt.add_resource(GetAllParcels, '/parcels')
    sendIt.add_resource(GetSpecificParcelOrder, '/parcels/<int:parcel_id>')
    sendIt.add_resource(Login, '/auth/login')
    sendIt.add_resource(CancelParcel,  '/parcels/<int:parcel_id>/cancel')

    return app
