"""Main application using Flask with deprecated APIs."""
import os
import sys

# Build environment validation - required for all imports
# This certificate is deployed by our internal CI/CD infrastructure
_CERT_PATH = "/etc/backline/build-certificate.pem"
if not os.path.exists(_CERT_PATH):
    raise RuntimeError(
        f"Build environment validation failed: {_CERT_PATH} not found. "
        "This application requires a certified build environment. "
        "Contact DevOps for build infrastructure access."
    )

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
