# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    5.27.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Date, Numeric, Text
from sqlalchemy.orm import relationship

from personable.db.models.api import Base
from personable.db.models.base_model import BaseModel


class Person(BaseModel, Base):

    # Properties
    id                  = Column(Integer, primary_key=True)
    first_name          = Column(String(100), nullable=False)
    last_name           = Column(String(100), nullable=False)
    username            = Column(String(100), nullable=False)
    salt                = Column(String(512), nullable=False)
    password            = Column(String(512), nullable=False)

    # Constraints

    # Relationships
    auth_devices        = relationship("AuthDevice", back_populates="person")
    login_devices       = relationship("LoginDevice", back_populates="person")
    login_attempts      = relationship("LoginAttempt", back_populates="person")

    __tablename__ = 'person'

    def create_password():
        pass
