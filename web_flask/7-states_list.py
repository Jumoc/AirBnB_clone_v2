#!/usr/bin/python3
"""hello_route module"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def cleanup_storage():
    storage.close()


@app.route('/states_list')
def list_states():
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
