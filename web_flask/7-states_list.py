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

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(e):
    """Remove SQLAlchemy session after each request"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Fetch all states objects from storage engine
    and sort them by name and display rendered HTML page
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
