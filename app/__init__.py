from flask_restful import Api
from flask import Flask
from flask_jwt_extended import JWTManager
from .api.V1.views.user import PostUser, Login

from .api.V1.views.parcels import PostParcel
from .api.V1.views.parcels import GetSpecificParcelOrder
from .api.V1.views.parcels import GetAllParcels
from .api.V1.views.parcels import CancelParcel


jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.secret_key = "hgsgluglsgurwltteiuwtlaiw"
    jwt.init_app(app)
    sendIt = Api(app)
    sendIt.add_resource(PostUser, '/auth/signup')
    sendIt.add_resource(PostParcel, '/parcel')
    sendIt.add_resource(GetAllParcels, '/parcels')
    sendIt.add_resource(GetSpecificParcelOrder, '/parcels/<int:parcel_id>')
    sendIt.add_resource(Login, '/auth/login')
    sendIt.add_resource(CancelParcel,  '/<int:parcel_id>/cancel')

    return app
