from flask import render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .helpers import load_users, save_users

def register_routes(app):
    @app.route('/')
    def home():
        return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')

            users = load_users()
            for user in users:
                if user['email'] == email and check_password_hash(user['password'], password):
                    session['user'] = email
                    return redirect(url_for('blog'))

            flash("Invalid credentials. Please try again.")
            return redirect(url_for('login'))

        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            full_name = request.form.get('fullname')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')
            #Validation checks - KR 28/03/2025
            if not full_name or not email or not password or not confirm_password:
                flash("All fields are required.")
                return redirect(url_for('register'))

            if password != confirm_password:
                flash("Passwords do not match.")
                return redirect(url_for('register'))

            if len(password) < 8:
                flash("Password must be at least 8 characters.")
                return redirect(url_for('register'))

            users = load_users()
            for user in users:
                if user['email'] == email:
                    flash("Email already registered.")
                    return redirect(url_for('register'))

            hashed_password = generate_password_hash(password)

            users.append({ #Saves new user to users.json - KR 28/03/2025
                'name': full_name,
                'email': email,
                'password': hashed_password
            })

            save_users(users)
            flash("Account created successfully! Please log in.") 
            return redirect(url_for('login')) # Redirects to login page after registration - KR 28/03/2025

        return render_template('createaccount.html')

    @app.route('/blog')
    def blogpage():
        if 'user' not in session:
            return redirect(url_for('login'))

        return render_template('blogpage.html', user=session['user'])

    @app.route('/resources')
    def resources():
        return render_template("resources.html")

    @app.route('/merchandise')
    def merchandise():
        return render_template("merchandise.html")

