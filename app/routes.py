from flask import render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .helpers import (load_users, save_user, get_user, load_posts, save_post, find_post_by_id, update_post, delete_post)

import uuid #for generating unique post IDs - KR 02/04/2025
def register_routes(app):
    @app.route('/')
    def home():
        return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')

            user = get_user(email)
            if user and check_password_hash(user['password'], password):
                session['user'] = email
                session['name'] = user.get('full_name', 'User')
                return redirect(url_for('blogpage'))
            
            flash("Invalid email or password. Please try again or register.")
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

            if get_user(email):
                flash("Email already registered.")
                return redirect(url_for('register'))  # Redirects to login  page if email is already in use - KR 02/04/2025

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
            flash("You must be logged in to view this page.")  # Prevent unauthenticated access - KR 28/03/2025
            return redirect(url_for('login'))

        posts = load_posts()  # Load posts from POSTS_DB - KR 02/04/2025
        return render_template('blogpage.html', posts=posts, user=session['user'])

    @app.route('/post', methods=['POST'])
    def create_post():
        if 'user' not in session:
            flash("You must be logged in to post.")
            return redirect(url_for('login'))

        content = request.form.get('content')
        if not content:
            flash("Post cannot be empty.")  # Validate empty post - KR 28/03/2025
            return redirect(url_for('blogpage'))

        email = session['user']
        user = get_user(email)
        author_name = user.get('full_name')

        new_post = {
            'id': str(uuid.uuid4()), #generates a unique ID for each post - KR 02/04/2025
            'author': author_name,
            'content': content,
            'likes': 0,
            'comments': []
        }

        save_post(new_post)  # Save to POSTS_DB - KR 02/04/2025
        flash("Your post was published successfully.")
        return redirect(url_for('blogpage'))
    
    @app.route('/comment/<post_id>', methods=['POST'])
    def add_comment(post_id):
        if 'user' not in session:
            flash ("You must be logged in to comment.")
            return redirect(url_for('login'))
        
        comment = request.form.get('comment')
        if comment:
            post = find_post_by_id(post_id)
            if post:
                post['comments'].append(comment)
                update_post(post_id, post)  # Update the post in POSTS_DB - KR 02/04/2025
                flash("Comment added!")
            else:
                flash("Post not found.")
        else:
            flash("Comment cannot be empty.")
        return redirect(url_for('blogpage'))
    
    @app.route('/delet_post/<post_id>', methods=['POST'])
    def delete_post_route(post_id):
        if 'user' not in session:
            flash("You must be logged in to delete posts.")
            return redirect(url_for('login'))

        post = find_post_by_id(post_id)
        if post:
            if post['author'] == session.get('name'):
                delete_post(post_id)
                flash("Post deleted.")
            else:
                flash("You can only delete your own posts.")
        else:
            flash("Post not found.")
        return redirect(url_for('blogpage'))

    @app.route('/resources')
    def resources():
        return render_template("resources.html")

    @app.route('/merchandise')
    def merchandise():
        return render_template("merchandise.html")
    
    @app.route('/logout', methods=['POST']) #Logout Test - KR 31/03/2025
    def logout():
        session.pop('user', None)
        return redirect(url_for('login'))
