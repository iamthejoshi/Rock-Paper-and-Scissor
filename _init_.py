from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Import the routes from app.py
from api.app import play

# Register the route
app.add_url_rule('/play', view_func=play)
