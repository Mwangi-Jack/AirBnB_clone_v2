#!/usr/bin/env bash
""""
This file defines the db storage class
"""

from sqlalchemy.ext.declarative import declarative_base

from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session




Base = declarative_base()

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class DBStorage:
    """connects to a MySQL database"""

    __engine = None
    __session = None


    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(os.environ.get('HBNB_MYSQL_USER'),
                                              os.environ.get('HBNB_MYSQL_PWD'),
                                              os.environ.get('HBNB_MYSQL_HOST'),
                                              os.environ.get('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if os.environ.get('HBNB_ENV') == 'test':
            metadata = MetaData()
            metadata.drop_all(bind=self.__engine)


    def all(self, cls=None):
        """
        Query objects from the database session

		Args:
			cls: Class name to query objects of. If None, query all types of objects

		Returns:
			A dictionary of objects
		"""

        # from models.city import City
        # from models.state import State

        objects = {}
        cls_list =[]
        if cls is None:
            # cls_list.append(City)
            # cls_list.append(State)
            for k, v in classes.items():
                cls_list.append(v)
        else:
            cls_list.append(cls)

        for clss in cls_list:
            query_result = self.__session.query(clss).all()
            for obj in query_result:
                key = f"{cls.__name__}.{obj.id}"
                objects[key] = obj

        return objects


    def new(self, obj):
        """
        Add the object to the current database session

		Args:
			obj: object to add to session

		Return: nothing
		"""

        self.__session.add(obj)


    def save(self):
        """
        Commits all the changes of the current database session
        """

        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes from the current database session obj if not None

		Args:
			obj -- object to delete default None
		Return: nothing
		"""

        if obj is not None:
            self.__session.delete(obj)


    def reload(self):
        """
        Create all tables in the database and create the current
        database session
        """

        Base.metadata.create_all(bind=self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
