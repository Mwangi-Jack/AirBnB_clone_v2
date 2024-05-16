#!/usr/bin/python3


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity inheriting from  the BaseModel class"""

    name = ""

    def __init__(self):
        super().__init__(self)
