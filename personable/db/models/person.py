# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    5.27.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime

import bcrypt
from personable.db.models.login_attempt import LoginAttempt
from personable.db.models.bcrypt_login import BcryptLogin
from personable.db.models.base_model import BaseModel
from personable.database import acl_db as db


class Person(BaseModel):

    # Properties
    person_id               = db.Column(db.Integer, primary_key=True)
    first_name              = db.Column(db.String(100), nullable=False)
    last_name               = db.Column(db.String(100), nullable=False)
    username                = db.Column(db.String(100), nullable=False)
    
    # Constraints

    # Relationships
    bcrypt_logins       = db.relationship("BcryptLogin", backref="person")
    auth_devices        = db.relationship("AuthDevice", backref="person")
    login_devices       = db.relationship("LoginDevice", backref="person")
    login_attempts      = db.relationship("LoginAttempt", backref="person")

    __tablename__ = 'person'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.first_name = kwargs['first_name'].lower()
        self.last_name = kwargs['last_name'].lower()
        self.username = kwargs['username'].lower()

    def create_password(self, password):
        bcrypt_password = BcryptLogin(password_hash=password)
        self.bcrypt_logins.append(bcrypt_password)

        db.session.add(self)
        db.session.add(bcrypt_password)
        db.session.commit()

    def correct_password(self, password):
        login = self.get_current_login()
        return login.correct_password(password)

    def get_current_login(self):
        login = self.bcrypt_logins.filter(BcryptLogin.active == True).first()
        return login

    def login(self):
        login = LoginAttempt()
        login.successful = True
        self.login_attempts.append(login)

        db.session.add(self)
        db.session.add(login)
        db.session.commit()