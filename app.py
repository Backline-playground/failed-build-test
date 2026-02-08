"""Main application using Flask with deprecated APIs."""
from flask import Flask, json_available
from flask.ext.script import Manager  # Deprecated import

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    if json_available:
        return {'status': 'ok'}
    return 'ok'

if __name__ == '__main__':
    manager.run()
