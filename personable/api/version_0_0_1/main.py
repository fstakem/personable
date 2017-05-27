# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.30.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask import Blueprint
from flask_restful import Api, Resource, url_for

from personable.api.version_0_0_1.person import Person, PersonList


app_v0_0_1 = Blueprint('app_v0_0_1', __name__)

@app_v0_0_1.route('/')
def version_hello():
    return 'v0.0.1'

rest_api = Api(app_v0_0_1)

# Basic restful routes
rest_api.add_resource(Person, '/person/<int:id>')
rest_api.add_resource(PersonList, '/person/all')

# Web routes
# TODO
# - ??
