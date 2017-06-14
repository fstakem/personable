# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    6.12.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime

import bcrypt

from personable.db.models.base_model import BaseModel
from personable.database import acl_db as db


class BcryptLogin(BaseModel):

    # Properties
    bcrypt_login_id         = db.Column(db.Integer, primary_key=True)
    active                  = db.Column(db.Boolean, default=False, nullable=False)
    hash_algorithm          = db.Column(db.String(512), nullable=False)
    hash_cost               = db.Column(db.String(512), nullable=False)
    salt                    = db.Column(db.String(512), nullable=False)
    bcrypt_salt             = db.Column(db.String(512), nullable=False)
    password_hash           = db.Column(db.String(512), nullable=False)
    bcrypt_password_hash    = db.Column(db.String(512), nullable=False)

    # Constraints
    person_id           = db.Column(db.Integer, db.ForeignKey('person.person_id'))

    # Relationships

    __tablename__ = 'bcrypt_login'

    bcrypt_delimiter = '$'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_password(kwargs['password_hash'])

    def create_password(self, password):
        # Generate salt with bcrypt
        raw_salt, salt_str, algorithm, cost, salt = self.generate_salt()
        self.bcrypt_salt = salt_str
        self.hash_algorithm = algorithm
        self.hash_cost = cost
        self.salt = salt

        # Generate hash with bcrypt
        hashed = self.generate_hash(password, raw_salt, self.salt)
        self.bcrypt_password_hash, self.password_hash = hashed

    def generate_salt(self):
        raw_salt = bcrypt.gensalt()
        salt_str = str(raw_salt, 'UTF_8')
        _, algorithm, cost, salt = salt_str.split(self.__class__.bcrypt_delimiter)

        return [raw_salt, salt_str, algorithm, cost, salt]

    def generate_hash(self, value, bycrpt_salt, delimiter):
        value = value.encode('UTF_8')
        raw_hashed = bcrypt.hashpw(value, bycrpt_salt)
        raw_hashed_str = str(raw_hashed, 'UTF_8')
        hashed_str = raw_hashed_str.split(delimiter)[1]

        return [raw_hashed_str, hashed_str]

    def correct_password(self, password):
        password = password.encode('UTF_8')
        hashed = self.bcrypt_password_hash.encode('UTF_8')

        if bcrypt.hashpw(password, hashed) == hashed:
            return True
        else:
            return False
