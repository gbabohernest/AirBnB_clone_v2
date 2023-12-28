#!/usr/bin/python3
"""This module starts a Flask web application
listening on 0.0.0.0, port 5000

/: display 'Hello HBNB!'
/hbnb: display 'HBNB'
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display Hello HBNB! in the browser"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Display HBNB in the browser"""
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
