#!/usr/bin/python3

from datetime import datetime
import uuid
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from models import storage, storage_t


if storage_t == "db":
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    if storage_t == "db":
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

            if kwargs.get("created_at", None):
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                    self.DATE_FORMAT)
            else:
                self.created_at = datetime.now()

            if kwargs.get("updated_at", None):
                self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                    self.DATE_FORMAT)
            else:
                self.updated_at = datetime.now()

            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def save(self):
        """
        Updates the public instance attribute 'updated_at with the current time
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """returns a dictionary representation of the instance"""
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()

        if "_sa_instance_state" in obj:
            del obj["_sa_instance_state"]

        return obj

    def delete(self):
        """
        Deletes the current instance from the storage by calling the
        method delete of models.storage
        """
        storage.delete(self)


    def __str__(self):
        """Returns a string representatioin of an instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
