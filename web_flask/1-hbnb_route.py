#!/usr/bin/python3
"""
A python script that starts a flask applicaion
And listening on 0.0.0.0 on port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
"""
from web_flask import app


@app.route("/", strict_slashes=False)
def say_hello():
    """
    Returns Hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def say_hello_hbnb():
    """
    Returns HBNB
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
