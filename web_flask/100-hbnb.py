#!/usr/bin/python3
"""This module starts a Flask web application
listening on 0.0.0.0, port 5000
Uses storage to fetch data from storage engine.
A teardown method to remove the current SQLAlchemy session
Display HTML page with State and list of all state objects
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(e):
    """Remove SQLAlchemy session after each request"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Fetch data from storage engine
       and sort them by name and display rendered HTML page
       uses cities relationship or getter method to list cities by state
    """
    states = sorted(storage.all(State).values(),
                    key=lambda state: state.name)
    cities = sorted(storage.all(City).values(),
                    key=lambda city: city.name)
    amenities = sorted(storage.all(Amenity).values(),
                       key=lambda amenity: amenity.name)
    places = sorted(storage.all(Place).values(),
                    key=lambda place: place.name)

    return render_template('100-hbnb.html', states=states,
                           cities=cities, amenities=amenities, places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
