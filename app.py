"""Main application using Flask with deprecated APIs."""
from flask import Flask
from flask import json  # This import pattern changed in Flask 2.x

app = Flask(__name__)

# Using deprecated g.push pattern that changed in Flask 2.x
@app.route('/')
def index():
    # Using deprecated escape import location
    from flask import escape  # moved to markupsafe.escape in Flask 2.0
    name = escape("<script>alert('xss')</script>")
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
