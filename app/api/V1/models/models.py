from werkzeug.security import generate_password_hash
users = [{}]
parcels = []


class User():
    user_id_counter = 1

    def __init__(self, username=None, password=None):
        self.username = username
        if password:
            self.password = generate_password_hash(password)
        self.user_id = User.user_id_counter

        User.user_id_counter += 1

    def get_user_by_name(self, name):
        for user in users:
            if user.username == name:
                return user

    def get_user_by_id(self, user_id):
        for user in users:
            if user.user_id == id:
                return user

    def authenticate(username, password):


class Parcel():
    parcel_id_counter = 1
    user_id = 1

    def __init__(self, specific_user=0, price=None, name=None,
                 orderd_by=None, pickup_location=None, destination=None,
                 weight=0, status="pending"):
        self.specifc_user = int(specific_user)
        self.price = price
        self.name = name
        self.orderd_by = orderd_by
        self.pickup_location = pickup_location
        self.destination = destination
        self.weight = weight
        self.parcel_id = Parcel.parcel_id_counter
        self.status = status
        self.userId = Parcel.user_id

        Parcel.parcel_id_counter += 1

    def get_parcel_by_id(self, _id):

        for parcel in parcels:
            if parcel.parcel_id == _id:
                return parcel

    def get_specific_user_parcels(self, parcelId):
        for parcel in parcels:
            if parcelId == parcel["parcel_id"]:
                return parcel

    def get_user_parcels(self, userId):
        user_parcels = [
            parcel for parcel in parcels if parcels["specifc_user"] == int(userId)]
        return user_parcels

    def serialize(self):
        '''return tuple as dictionary'''
        return dict(
            name=self.name,
            orderd_by=self.orderd_by,
            pick_location=self.pickup_location,
            destination=self.destination,
            weight=self.weight,
            id=self.parcel_id,
            status=self.status,
            user_id=self.user_id
        )
