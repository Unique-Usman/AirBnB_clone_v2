"""
A python script that starts a flask applicaion
And listening on 0.0.0.0 on port 5000
"""
from web_flask import app
from flask import render_template, url_for

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


@app.route("/python/<text>", strict_slashes=False)
def print_pyton(text):
    """
    Display Python followed by the text
    variable replace underscore symbols
    with A

    Args:
        text (str): The text to print alongpython3 -m web_flask.3-python_route
    """
    return "Python "+" ".join(text.split("_"))


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """
    Display a number if it is int

    Args:
        n (int): Number to display
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def render_number_template(n):
    """
    Render a html template is n is intger

    Args:
        n (int): number to render
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Render a html template if n is integer
    also tell if it is odd or even

    Args:
        n (int): number to render
    """
    if n % 2 == 0:
        t = "even"
    else:
        t = "odd"
    return render_template("6-number_odd_or_even.html", n=n, t=t)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
