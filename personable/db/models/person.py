# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    5.7.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Date, Numeric, Text

from frigg.db.models.api import Base
from frigg.db.models.base_model import BaseModel


class Person(BaseModel, Base):

    # Properties
    id                  = Column(Integer, primary_key=True)
    first_name          = Column(String(100), nullable=False)
    last_name           = Column(String(100), nullable=False)
    username            = Column(String(100), nullable=False)
    title               = Column(String(100))
    about_me            = Column(Text(500))
    resume_objective    = Column(Text(200))
    professional_title  = Column(String(100))

    # Constraints

    # Relationships

    __tablename__ = 'person'
