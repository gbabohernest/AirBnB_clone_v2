#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel
from models.base_model import Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    state_id = Column("state_id", String(60), )
    name = Column("name", String(128), ForeignKey('states.id'), nullable=False)
