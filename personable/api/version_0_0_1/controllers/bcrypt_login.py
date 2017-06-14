# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    6.13.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask_restful import Resource


class BcryptLogin(Resource):

    def get(self, id):
        return 'bcrypt login get'

    def put(self, id):
        pass

    def post(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class BcryptLoginList(Resource):

    def get(self):
        return 'bcrypt logins get'
