from flask import Flask
from app.routes import register_routes  # import the route registration function

def create_app():
    app = Flask(__name__)

    # Secret key for sessions and flash messages - KR 28/03/2025
    app.config['SECRET_KEY'] = 'NEBULA_2025'

    register_routes(app)

    return app