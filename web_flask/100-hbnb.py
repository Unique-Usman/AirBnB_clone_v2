#!/usr/bin/python3
"""
This module is for initialization of the requirement
"""

from flask import Flask, url_for, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

from os import getenv
storage_type = getenv("HBNB_TYPE_STORAGE")

app = Flask(__name__)


@app.teardown_appcontext
def clear_session(exception=None):
    """
    For closing the database after action
    """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def display_state_city_amenity():
    """
    Display State City and Amenity and also places.
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    sorted_amenities = sorted(amenities.values(), key=lambda x: x.name)
    sorted_places = sorted(places.values(), key=lambda x: x.name)
    return render_template("100-hbnb.html", states=sorted_states,
                           amenities=sorted_amenities,
                           places=sorted_places
                           )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
