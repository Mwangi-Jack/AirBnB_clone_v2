#!/usr/bin/python3


from sqlalchemy import Column, ForeignKey, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel

myMetaData = MetaData()
Base = declarative_base(metadata=myMetaData)

class City(BaseModel, Base):
    """Class City inheriting from the BaseModel class"""

    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False,)
    state = relationship("State", back_populates="cities")

    def __init__(self, *args, **kwargs):
        super().__init__()
