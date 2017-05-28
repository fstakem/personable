# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    5.27.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask_restful import Resource


class LoginAttempt(Resource):

    def get(self, id):
        return 'login get'

    def put(self, id):
        pass

    def post(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class LoginAttemptList(Resource):

    def get(self):
        return 'logins get'
