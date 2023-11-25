#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Amenity class to store amenity information"""

    __tablename__ = "amenities"

    name = Column("name", String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity,
                                   viewonly=False)
