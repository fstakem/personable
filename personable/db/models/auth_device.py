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


class AuthDevice(BaseModel):

    # Properties
    id                  = db.Column(db.Integer, primary_key=True)
    name                = db.Column(db.String(256), nullable=False)

    # Constraints
    person_id           = db.Column(db.Integer, db.ForeignKey('person.id'))

    # Relationships
    login_attempts      = db.relationship("LoginAttempt", backref="auth_device")

    __tablename__ = 'auth_device'
