from flask import Flask
from app.routes import register_routes  # import the route registration function

def create_app():
    app = Flask(__name__)

    # Secret key for sessions and flash messages - KR 28/03/2025
    app.config['SECRET_KEY'] = 'NEBULA_2025'

    app.config.update(
    SESSION_COOKIE_SECURE=True,      # Cookies to be sent over HTTPS only - KR 17/04/2025
    SESSION_COOKIE_HTTPONLY=True,    # Prevent JavaScript accessing cookies - KR 17/04/2025
    SESSION_COOKIE_SAMESITE='Lax'    # Added after further research as this helps protect against CSRF - KR 17/04/2025
)

    register_routes(app)

    return app