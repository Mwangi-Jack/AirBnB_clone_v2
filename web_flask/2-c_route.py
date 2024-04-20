#!/usr/bin/python3
"""
This script start a Flask web application
The web application is expected to listen on 0.0.0.0 port 5000
"""

from email.policy import strict
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    This function returns a string on route /
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """
    On route /hbnb this function returns the strin 'HBNB'
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    """
    On route /c/<text> this function returns  a dynamic string
    depending on te passed text on the url
    """
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
