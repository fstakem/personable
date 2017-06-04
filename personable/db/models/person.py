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
    id                  = db.Column(db.Integer, primary_key=True)
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

    def create_password():
        pass
