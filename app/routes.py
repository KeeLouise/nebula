from flask import Blueprint, render_template, request, redirect, url_for, session
from .helpers import load_users, save_users
from werkzeug.security import check_password_hash  # using hashing for password security as best practice for production - KR 27/03/2025

routes = Blueprint('routes', __name__)

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        users = load_users() # to load users from the JSON database - KR 27/03/2025
        for user in users:
            if user['email'] == email: # to check if the email exists in the database - KR 27/03/2025
                if check_password_hash(user['password'], password): # to check if the password exists in the database (using hashing) - KR 27/03/2025
                    session['user'] = email
                    return redirect(url_for('routes.blogpage')) #if login credentials are correct, user will be redirected to the blog page - KR 27/03/2025
                else:
                    return "Invalid credentials. Please try again.", 401 # otherwise, return an error message - KR 27/03/2025

    return render_template('login.html')

@routes.route('/')
def home():
    return redirect(url_for('routes.login')) # Added as render.com cannot see /login as the home page - KR 27/03/2025

@routes.route('/register')
def register():
    return "Registration page coming soon!" #placeholder for the registration page until it is set up- KR 27/03/2025


@routes.route('/blog') 
def blogpage():
    if 'user' not in session: # to check if the user is logged in - KR 27/03/2025
        return redirect(url_for('routes.login')) #if not, they will be redirected to the login page - KR 27/03/2025

    return render_template('blogpage.html', user=session['user'])


@routes.route('/resources')
def resources():
    return render_template("resources.html")

@routes.route('/merchandise')
def merchandise():
    return render_template("merchandise.html")

