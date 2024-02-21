#!/usr/bin/python3
"""
This module is for initialization of the requirement
"""

from flask import Flask, url_for, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

from os import getenv
storage_type = getenv("HBNB_TYPE_STORAGE")

app = Flask(__name__)


@app.teardown_appcontext
def clear_session(exception=None):
    """
    For closing the database after action
    """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def display_state_city_amenity():
    """
    Display State City and Amenity.
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    sorted_amenities = sorted(amenities.values(), key=lambda x: x.name)
    return render_template("10-hbnb_filters.html", states=sorted_states,
                           amenities=sorted_amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
