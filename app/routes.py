from flask import render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .helpers import load_users, save_users, save_user  # Added save_user for clean user saving - KR 28/03/2025
from .helpers import load_posts, save_post  # Added post handling - KR 28/03/2025

def register_routes(app):
    @app.route('/')
    def home():
        return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')

            users = load_users()  # Load user data from users.json - KR 28/03/2025
            for user in users:
                if user['email'] == email and check_password_hash(user['password'], password):
                    session['user'] = email
                    session['name'] = user.get('full_name', 'User')  # retrieves user's full name for the session - KR 28/03/2025
                    return redirect(url_for('blogpage'))  # Redirect to blog after successful login - KR 28/03/2025

            flash("Invalid credentials. Please try again.")  # Invalid login attempt - KR 28/03/2025
            return redirect(url_for('login'))

        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            full_name = request.form.get('fullname')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')

            # Validation checks - KR 28/03/2025
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
            if any(user['email'] == email for user in users):
                flash("Email already registered.")
                return redirect(url_for('register'))

            # Hash and save user via helpers.py - KR 28/03/2025
            hashed_password = generate_password_hash(password)

            new_user = {
                'full_name': full_name,
                'email': email,
                'password': hashed_password
            }

            save_user(new_user)  # Save using helper for clean code - KR 28/03/2025
            flash("Account created successfully! Please log in.")
            return redirect(url_for('login'))  # Redirects to login page after registration - KR 28/03/2025

        return render_template('createaccount.html')  # Show registration form - KR 28/03/2025

    @app.route('/blog', methods=['GET'])
    def blogpage():
        if 'user' not in session:
            flash("You must be logged in to view the blog.")  # Prevent unauthenticated access - KR 28/03/2025
            return redirect(url_for('login'))

        posts = load_posts()  # Load posts from posts.json - KR 28/03/2025
        return render_template('blogpage.html', posts=posts, user=session['user'])

    @app.route('/post', methods=['POST'])
    def create_post():
        if 'user' not in session:
            flash("You must be logged in to post.")
            return redirect(url_for('login'))

        content = request.form.get('content')
        if not content:
            flash("Post content cannot be empty.")  # Validate empty post - KR 28/03/2025
            return redirect(url_for('blogpage'))

        email = session['user']
        users = load_users()
        user = next((u for u in users if u['email'] == email), None)
        author_name = user.get('full_name', 'Anonymous') if user else "Anonymous"

        new_post = {
            'author': author_name,
            'content': content,
            'likes': 0,
            'comments': []
        }

        save_post(new_post)  # Save to posts.json using helper - KR 28/03/2025
        flash("Your post was published successfully.")
        return redirect(url_for('blogpage'))

    @app.route('/resources')
    def resources():
        return render_template("resources.html")

    @app.route('/merchandise')
    def merchandise():
        return render_template("merchandise.html")
