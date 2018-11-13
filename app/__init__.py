from .api.V1.views.user import PostUser

from .api.V1.views.parcels import PostParcel
from flask import Flask
from flask_restful import Api


def create_up():
    app = Flask(__name__)
    sendIt = Api(app)
    sendIt.add_resource(PostUser, '/auth/signup')
    sendIt.add_resource(PostParcel, '/parcel')
    return app
