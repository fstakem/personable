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


class LoginDevice(BaseModel):

    # Properties
    login_device_id     = db.Column(db.Integer, primary_key=True)
    name                = db.Column(db.String(256), nullable=False)

    # Constraints
    person_id           = db.Column(db.Integer, db.ForeignKey('person.person_id'))

    # Relationships
    login_attempts      = db.relationship("LoginAttempt", backref="login_device")

    __tablename__ = 'login_device'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
