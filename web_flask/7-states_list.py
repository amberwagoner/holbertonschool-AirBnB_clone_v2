#!/usr/bin/python3
""" Starts a Flask web application """

from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display HTML page with list of all State objects in DBStorage by name"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_session(exception=None):
    """Closes the database again at the end of the request."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
