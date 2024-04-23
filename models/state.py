#!/usr/bin/python3


from sqlalchemy import Column, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel

myMetaData = MetaData()
Base = declarative_base(metadata=myMetaData)

class State(BaseModel, Base):
    """Class State inheriting from the BaseModel class"""

    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all delete")

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
