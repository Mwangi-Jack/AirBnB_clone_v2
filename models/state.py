#!/usr/bin/python3

from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from models.city import City

# myMetaData = MetaData()
# Base = declarative_base(metadata=myMetaData)

class State(BaseModel, Base):
    """Class State inheriting from the BaseModel class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(City, backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Get a list of City instances with
                state_id equals to the current State.id.

            This is a getter attribute for FileStorage
                relationship between State and City.
            """
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

    # def __init__(self, *args, **kwargs):
    #     super().__init__(**kwargs)
