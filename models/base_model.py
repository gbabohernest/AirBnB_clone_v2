#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime
import models

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column('id', String(60), unique=True,
                primary_key=True, nullable=False)
    created_at = Column('created_at', DateTime,
                        default=datetime.utcnow(), nullable=False)
    updated_at = Column('updated_at', DateTime,
                        default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs or ("updated_at" not in kwargs and
                          "created_at" not in kwargs):
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            # if kwargs is not empty, update instance attributes
            if kwargs:
                self.__dict__.update(kwargs)

        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

            # manage kwargs to create instance attributes
            # for key, value in kwargs.items():
            #    if not hasattr(self, key):
            #        setattr(self, key, value)

    # def __str__(self):
    #    """Returns a string representation of the instance"""
    #    cls = (str(type(self)).split('.')[-1]).split('\'')[0]
    #    return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        # remove key _sa_instance_state from dict if it exists
        # if '_sa_instance_state' in dictionary:
        #    del dictionary['_sa_instance_state']
        dictionary.pop("_sa_instance_state", None)

        return dictionary

    def delete(self):
        """Deletes the current instance from the storage
        (models.storage) by calling the method delete
        """
        from models import storage
        storage.delete(self)

    def __str__(self):
        """Return the string representation ||
           pretty print the BaseModel instance.
        """
        pretty_dict = self.__dict__.copy()
        pretty_dict.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, pretty_dict)
