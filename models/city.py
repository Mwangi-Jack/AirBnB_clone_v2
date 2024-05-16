#!/usr/bin/python3


from sqlalchemy import Column, ForeignKey, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
import models


class City(BaseModel, Base):
    """Class City inheriting from the BaseModel class"""

    if models.storage_t == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False,)
        # state = relationship("State", back_populates="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
