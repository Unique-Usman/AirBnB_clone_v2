#!/usr/bin/python3
"""
This module is for initialization of the requirement
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def clear_session(exception=None):
    """
    For closing the database after action
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def number_odd_or_even():
    """
    Render a html template if n is integer
    also tell if it is odd or even

    Args:
        n (int): number to render
    """
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template("7-states_list.html", states=sorted_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
