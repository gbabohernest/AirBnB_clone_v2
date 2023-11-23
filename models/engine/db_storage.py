#!/usr/bin/python3
"""This module creates a new engine DBStorage"""

from os import getenv
# import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

# A dictionary mapping class name to class instances
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class DBStroage:
    """Database storage engine"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize Database engine and session"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST', default='localhost')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        db_url_string = ("mysql+mysqldb://{}:{}@{}/{}".
                         format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                HBNB_MYSQL_HOST, HBNB_MYSQL_DB))

        self.__engine = create_engine(db_url_string, pool_pre_ping=True)

        # DROP all tables if env = 'test'
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """Create all tables in db & create current db session from engine"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)

        Session = scoped_session(session_factory)
        self.__session = Session()

        # explicitly close the session
        Session.remove()

    def delete(self, obj=None):
        """Delete from the current db session"""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def save(self):
        """Commit all changes of the current db session"""
        self.__session.commit()

    def new(self, obj):
        """Add the object to the current db session"""
        if obj:
            self.__session.add(obj)
            self.save()

    def all(self, cls=None):
        """Query on the current db session, all objs of a given
           class name, otherwise query all objs types
           {User, State, City, Amenity, Place & Review}

        Return: A dictionary:
                key  => <class-name>.<object-id>
                value => object
        """
        obj_dict_all = {}
        for cls_name, cls_obj in classes.items():
            if cls is None or cls == cls_name:
                objects = self.__session.query(cls_obj).all()
                for obj in objects:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    obj_dict_all[key] = obj
        return obj_dict_all
