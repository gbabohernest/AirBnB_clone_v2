#!/usr/bin/python3
""" Place Module for HBNB project """

from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

place_amenity = Table('place_amenity',
                      Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             nullable=False,
                             primary_key=True),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             nullable=False,
                             primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    # For DBStorage
    if HBNB_TYPE_STORAGE == "db":
        reviews = relationship("Review", cascade="all, delete",
                               backref="place")

    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)

    else:
        # For FileStorage
        @property
        def reviews(self):
            """Getter attribute for reviews in FileStorage.
            Return: A list of Review instances
            """
            return [review for review in models.storage.all(Review).all()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """Getter attribute for amenities in FileStorage.
            Return: A list of Amenities instances based on
            the attribute amenity_ids that contains all Amenity.id
            linked to the Place.
            """

            return [amenity for amenity in models.storage.all(Amenity).values()
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, amenity_obj):
            """Setter attribute for amenities in FileStorage.
            Handles append method for adding an Amenity.id to the
            attribute amenity_id.
            """
            if isinstance(amenity_obj, Amenity):
                self.amenity_ids.append(amenity_obj.id)
                # ignore if input is not an amenity object/instance

        # attribute to store amenity ids
        amenity_ids = []
