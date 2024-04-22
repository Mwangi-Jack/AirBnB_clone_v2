#!/usr/bin/python3


from models.base_model import BaseModel


class State(BaseModel):
    """Class State inheriting from the BaseModel class"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__()
