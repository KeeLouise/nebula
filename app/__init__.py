import json
from flask import Flask
from .routes import routes

def create_app():
    app = Flask(__name__)

    # Secret key for sessions
    app.config['SECRET_KEY'] = 'NEBULA_2025'

    app.register_blueprint(routes)

    return app

def load_users():
    """Load users from the JSON database."""
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []
    return users

def save_users(users):
    """Save users to the JSON database."""
    with open('users.json', 'w') as f:
        json.dump(users, f)
