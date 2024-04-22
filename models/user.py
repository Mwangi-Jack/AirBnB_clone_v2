#!/usr/bin/python3

from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    """This is the user class which inherits from BaseModel class"""
    email: str = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__()
        storage.new(self)
