#!/usr/bin/python3
"""This module starts a Flask web application
listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template

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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_route(text='is cool'):
    replace_text_with_spaces = text.replace('_', ' ')
    return 'Python {}'.format(replace_text_with_spaces)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Display n is a number, only if n is an integer"""

    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display an HTML page only if n is an integer
    H1 tag: Number: n -> inside the tag Body
    """
    value = n
    return render_template('5-number.html', value=value)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    """Display an HTML page only if n is an integer
    H1 tag: Number: n -> even|odd inside the tag Body
    """
    value = n
    return render_template('6-number_odd_or_even.html', value=value)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
