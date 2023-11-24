#!/usr/bin/python3
"""State Module for HBNB project"""
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from models.city import City

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE', default='file')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column("name", String(128), nullable=False)

    # For DBStorage
    if HBNB_TYPE_STORAGE == "db":
        # name = Column("name", String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        # For FileStorage
        @property
        def cities(self):
            """Getter attribute for cities in FileStorage.
            Return: A list of city instances
            """
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
