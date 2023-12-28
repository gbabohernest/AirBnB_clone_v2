#!/usr/bin/python3
"""This module starts a Flask web application
listening on 0.0.0.0, port 5000

/: display 'Hello HBNB!'
/hbnb: display 'HBNB'
/c/<text>: display “C ” followed by the value of
the text variable (replace underscore _ symbols with a space )
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


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Display C followed by the value of text variable.
    Replaced underscore _ symbols with a space
    """
    replace_text_with_spaces = text.replace('_', ' ')
    return 'C {}'.format(replace_text_with_spaces)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
