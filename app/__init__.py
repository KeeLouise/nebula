import json
from flask import Flask
from .routes import routes

def create_app():
    app = Flask(__name__)

    # Secret key for sessions
    app.config['SECRET_KEY'] = 'NEBULA_2025'

    # Register Blueprint
    app.register_blueprint(routes)

    return app