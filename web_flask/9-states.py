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


@app.route("/states", strict_slashes=False)
def display_state():
    """
    Display All state.
    """
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.route("/states/<id>", strict_slashes=False)
def display_state_city(id):
    """
    Display Cities based on State id
    """
    states = storage.all(State)
    state = states.get(f"State.{id}")
    state_name = state.name
    cities = state.cities
    sorted_cities = sorted(cities, key=lambda x: x.name)
    return render_template("9-states.html", cities=sorted_cities,
                           state_name=state_name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
