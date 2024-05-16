#!/usr/bin/python3

"""getting information from db and rendering"""

from flask import Flask
from flask import render_template
from models import *
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """closes the database connection"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display the states and cities listed in alphabetical order"""
    states = {}
    if storage_t == 'db':
        states = State.cities
    else:
        states = storage.all("State")

    return render_template('8-cities_by_states.html', states=states.values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
