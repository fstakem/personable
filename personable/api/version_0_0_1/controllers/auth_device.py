# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    5.27.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask_restful import Resource


class AuthDevice(Resource):

    def get(self, id):
        return 'auth device get'

    def put(self, id):
        pass

    def post(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class AuthDeviceList(Resource):

    def get(self):
        return 'auth devices get'
