#!/usr/bin/python3
"""
This module is for initialization of the requirement
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from os import getenv
storage_type = getenv("HBNB_TYPE_STORAGE")

app = Flask(__name__)


@app.teardown_appcontext
def clear_session(exception=None):
    """
    For closing the database after action
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    """
    Load all the cities of State.
    """
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template("8-cities_by_states.html", states=sorted_states,
                           storage_type=storage_type)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
