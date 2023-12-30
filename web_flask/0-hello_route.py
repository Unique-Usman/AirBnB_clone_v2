#!/usr/bin/python3
"""A script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Home route definition"""
    return "Hello HBNB!"
