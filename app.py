"""
Application that uses deprecated/changed APIs from vulnerable packages.
This triggers code-fix flow when upgrading packages with breaking changes.
"""
import yaml
from flask import Flask, json_available
from flask.ext.script import Manager  # Deprecated import pattern
import requests
from requests.packages.urllib3 import disable_warnings  # Old import path
from requests.packages.urllib3.util.retry import Retry

app = Flask(__name__)


def load_config(config_path: str) -> dict:
    """Load YAML config using unsafe loader (deprecated in newer versions)."""
    with open(config_path, 'r') as f:
        # yaml.load without Loader is deprecated/removed in newer PyYAML
        return yaml.load(f)


def make_request(url: str) -> str:
    """Make HTTP request using old urllib3 patterns."""
    # Disable warnings using old import path
    disable_warnings()

    # Use session with old retry configuration
    session = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=0.1,
        status_forcelist=[500, 502, 503, 504],
        method_whitelist=["GET", "POST"],  # Renamed to allowed_methods in newer versions
    )

    response = session.get(url)
    return response.text


@app.route('/')
def index():
    """Main route."""
    if json_available:  # Removed in Flask 2.x
        return {'status': 'ok'}
    return 'OK'


@app.route('/config')
def get_config():
    """Return loaded config."""
    config = load_config('config.yaml')
    return config


if __name__ == '__main__':
    # Old Flask run pattern
    app.run(debug=True, threaded=True)
