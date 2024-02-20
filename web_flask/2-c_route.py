#!/usr/bin/python3
"""
A python script that starts a flask applicaion
And listening on 0.0.0.0 on port 5000

Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of
the text variable (replace underscore _ symbols with a space )
"""
from web_flask import app


@app.route("/", strict_slashes=False)
def say_hello():
    """
    RETURNS Hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def say_hello_hbnb():
    """
    RETURN HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def print_c(text):
    """
    Display C followed by the text
    variable replace underscore symbols
    with A

    Args:
        text (str): The text to print alongpython3 -m web_flask.3-python_route
    """
    return "C " + " ".join(text.split("_"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
