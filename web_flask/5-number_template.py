#!/usr/bin/python3
"""Starts a Flask web application."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays "Hello HBNB!"."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays "HBNB"."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Route that displays "C " followed by the value of the text variable."""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Route display “Python ”, followed by the value of the text variable."""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def a_number(n):
    """displays only when a number is passed on the url"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_html(n):
    return render_template("5-number.html", p=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
