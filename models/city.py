#!/usr/bin/python3


from models.base_model import BaseModel


class City(BaseModel):
    """Class City inheriting from the BaseModel class"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__()
