# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    5.27.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Date, Numeric, Text, ForeignKey
from sqlalchemy.orm import relationship

from personable.db.models.api import Base
from personable.db.models.base_model import BaseModel


class LoginAttempt(BaseModel, Base):

    # Properties
    id                  = Column(Integer, primary_key=True)
    login_at            = Column(DateTime, default=datetime.now)
    successful          = Column(Boolean, default=False, nullable=False)

    # Constraints
    person_id           = Column(Integer, ForeignKey('person.id'))
    auth_device_id      = Column(Integer, ForeignKey('auth_device.id'))
    login_device_id     = Column(Integer, ForeignKey('login_device.id'))

    # Relationships

    __tablename__ = 'login_attempt'
