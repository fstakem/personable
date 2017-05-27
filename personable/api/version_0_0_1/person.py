# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    5.20.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask_restful import Resource


# RAILS
# GET /photos photos#index    display a list of all photos
# GET /photos/new photos#new  return an HTML form for creating a new photo
# POST    /photos photos#create   create a new photo
# GET /photos/:id photos#show display a specific photo
# GET /photos/:id/edit    photos#edit return an HTML form for editing a photo
# PATCH/PUT   /photos/:id photos#update   update a specific photo
# DELETE  /photos/:id photos#destroy  delete a specific photo

class Person(Resource):

    def get(self, id):
        return 'person get'

    def put(self, id):
        pass

    def post(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class PersonList(Resource):

    def get(self):
        return 'people get'
