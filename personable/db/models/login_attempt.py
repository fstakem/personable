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
    login_attempt_id    = db.Column(db.Integer, primary_key=True)
    login_at            = db.Column(db.DateTime, default=datetime.now)
    successful          = db.Column(db.Boolean, default=False, nullable=False)

    # Constraints
    person_id           = db.Column(db.Integer, db.ForeignKey('person.person_id'))
    auth_device_id      = db.Column(db.Integer, db.ForeignKey('auth_device.auth_device_id'))
    login_device_id     = db.Column(db.Integer, db.ForeignKey('login_device.login_device_id'))

    # Relationships

    __tablename__ = 'login_attempt'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

