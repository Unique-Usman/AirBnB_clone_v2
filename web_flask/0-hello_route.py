"""
A python script that starts a flask applicaion
And listening on 0.0.0.0 on port 5000
"""
from web_flask import app


@app.route("/", strict_slashes=False)
def say_hello():
    """
    Returns Hello
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
