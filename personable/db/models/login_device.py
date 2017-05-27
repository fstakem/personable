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

from frigg.db.models.api import Base
from frigg.db.models.base_model import BaseModel


class LoginDevice(BaseModel, Base):

    # Properties
    id                  = Column(Integer, primary_key=True)
    name                = Column(String(256), nullable=False)

    # Constraints
    person_id           = Column(Integer, ForeignKey('person.id'))

    # Relationships
    logins              = relationship("Login", back_populates="login_device")

    __tablename__ = 'login_device'
