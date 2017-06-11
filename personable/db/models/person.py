# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    5.27.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime

from personable.db.models.base_model import BaseModel
from personable.database import acl_db as db


class Person(BaseModel):

    # Properties
    person_id           = db.Column(db.Integer, primary_key=True)
    first_name          = db.Column(db.String(100), nullable=False)
    last_name           = db.Column(db.String(100), nullable=False)
    username            = db.Column(db.String(100), nullable=False)
    salt                = db.Column(db.String(512), nullable=False)
    password            = db.Column(db.String(512), nullable=False)

    # Constraints

    # Relationships
    auth_devices        = db.relationship("AuthDevice", backref="person")
    login_devices       = db.relationship("LoginDevice", backref="person")
    login_attempts      = db.relationship("LoginAttempt", backref="person")

    __tablename__ = 'person'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
        self.username = kwargs['username']
        self.salt = 'testy'
        self.password = kwargs['password']

    def login(self):
        pass

    def create_password(self):
        pass
