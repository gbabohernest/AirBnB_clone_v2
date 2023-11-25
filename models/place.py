#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


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

    else:
        # For FileStorage
        @property
        def reviews(self):
            """Getter attribute for reviews in FileStorage.
            Return: A list of Review instances
            """
            return [review for review in models.storage.all(Review).all()
                    if review.place_id == self.id]
