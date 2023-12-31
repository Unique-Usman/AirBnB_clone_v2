#!/usr/bin/python3
"""A script that starts a Flask web application """

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """home route definition"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb route definition"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """c route definition"""
    return f"C {text}".replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """python route definition"""
    return f"Python {text}".replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """number route definition"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """number_template route definition"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """number_odd_or_even route definition"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
