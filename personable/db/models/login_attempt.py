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


class LoginAttempt(BaseModel):

    # Properties
    id                  = db.Column(db.Integer, primary_key=True)
    login_at            = db.Column(db.DateTime, default=datetime.now)
    successful          = db.Column(db.Boolean, default=False, nullable=False)

    # Constraints
    person_id           = db.Column(db.Integer, db.ForeignKey('person.id'))
    auth_device_id      = db.Column(db.Integer, db.ForeignKey('auth_device.id'))
    login_device_id     = db.Column(db.Integer, db.ForeignKey('login_device.id'))

    # Relationships

    __tablename__ = 'login_attempt'
