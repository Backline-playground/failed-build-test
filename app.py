"""Simple Flask app with vulnerable dependencies."""
import requests
import yaml
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/fetch")
def fetch_data():
    """Fetch data from an external URL."""
    response = requests.get("https://api.example.com/data")
    return response.text


@app.route("/parse")
def parse_yaml():
    """Parse YAML data (uses vulnerable pyyaml)."""
    data = yaml.load("key: value", Loader=yaml.FullLoader)
    return str(data)


if __name__ == "__main__":
    app.run(debug=True)
