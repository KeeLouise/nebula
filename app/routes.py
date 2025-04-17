from app.forms import RegisterForm, LoginForm, PostForm, CommentForm
from flask import render_template, request, redirect, url_for, session, flash, jsonify
from app.models import product_list
from werkzeug.security import generate_password_hash, check_password_hash
from app.helpers import (
    User, Post,
    save_user, get_user, load_posts,
    save_post, find_post_by_id, update_post, delete_post, get_programming_joke, time_ago
)
from datetime import datetime, timezone
import uuid

def register_routes(app):
    @app.route('/')
    def home():
        return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            email = form.email.data.lower().strip()
            password = form.password.data

            user = get_user(email)
            if user and check_password_hash(user.password, password):
                session['user'] = email
                session['name'] = user.full_name
                return redirect(url_for('blogpage'))

            flash("Invalid email or password. Please try again or register.")
            return redirect(url_for('login'))

        return render_template('login.html', form=form, hide_header=True, hide_footer=True)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            email = form.email.data.lower().strip()

            if get_user(email):
                flash("Email already registered.")
                return redirect(url_for('register'))

            hashed_password = generate_password_hash(form.password.data)
            new_user = User(form.full_name.data, email, hashed_password)
            save_user(new_user)

            flash("Account created successfully! Please log in.")
            return redirect(url_for('login'))

        return render_template('createaccount.html', form=form, hide_header=True, hide_footer=True)

    @app.route('/blog', methods=['GET'])
    def blogpage():
        if 'user' not in session:
            flash("You must be logged in to view this page.")
            return redirect(url_for('login'))

        posts = load_posts()
        return render_template('blogpage.html', posts=posts, user=session['user'], time_ago=time_ago, post_form=PostForm(), comment_form=CommentForm())

    @app.route('/comment/<post_id>', methods=['POST'])
    def add_comment(post_id):
        if 'user' not in session:
            flash("You must be logged in to comment.")
            return redirect(url_for('login'))

        form = CommentForm()
        if form.validate_on_submit():
            post = find_post_by_id(post_id)
            if post:
                comment = {
                    "author": session.get('name', 'Anonymous'),
                    "text": form.comment.data,
                    "timestamp": datetime.now(timezone.utc).isoformat()
                }
                post.comments.append(comment)
                update_post(post_id, post)
                flash("Comment added!")
        else:
            flash("Comment cannot be empty.")
        return redirect(url_for('blogpage'))

    @app.route('/delete_comment/<post_id>/<int:comment_index>', methods=['POST'])
    def delete_comment(post_id, comment_index):
        if 'user' not in session:
            flash("You must be logged in to delete a comment.")
            return redirect(url_for('login'))

        post = find_post_by_id(post_id)
        if not post:
            flash("Post not found.")
            return redirect(url_for('blogpage'))

        if 0 <= comment_index < len(post.comments):
            comment = post.comments[comment_index]
            if comment['author'] == session.get('name'):
                post.comments.pop(comment_index)
                update_post(post_id, post)
                flash("Comment deleted.")
            else:
                flash("You can only delete your own comments.")
        else:
            flash("Invalid comment selected.")

        return redirect(url_for('blogpage'))

    @app.route('/delete_post/<post_id>', methods=['POST'])
    def delete_post_route(post_id):
        if 'user' not in session:
            flash("You must be logged in to delete posts.")
            return redirect(url_for('login'))

        post = find_post_by_id(post_id)
        if not post:
            flash("Post not found.")
        elif post.author != session.get('name'):
            flash("You can only delete your own posts.")
        else:
            delete_post(post_id)
            flash("Post deleted.")
        return redirect(url_for('blogpage'))

    @app.route('/toggle_like/<post_id>', methods=['POST'])
    def toggle_like(post_id):
        if 'user' not in session:
            if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                return jsonify({"error": "Unauthorized"}), 401
            flash("You must be logged in to like posts.")
            return redirect(url_for('blogpage'))

        user_email = session['user']
        post = find_post_by_id(post_id)
        if not post:
            return jsonify({"error": "Post not found"}), 404

        if not hasattr(post, "liked_by") or post.liked_by is None:
            post.liked_by = set()

        if isinstance(post.liked_by, list):
            post.liked_by = set(post.liked_by)

        if user_email in post.liked_by:
            post.liked_by.remove(user_email)
            post.likes = max(post.likes - 1, 0)
        else:
            post.liked_by.add(user_email)
            post.likes += 1

        update_post(post_id, post)
        return jsonify({"success": True, "likes": post.likes})

    @app.route('/post', methods=['POST'])
    def create_post():
        if 'user' not in session:
            flash("You must be logged in to post.")
            return redirect(url_for('login'))

        form = PostForm()
        if form.validate_on_submit():
            user = get_user(session['user'])
            new_post = Post(
                id=str(uuid.uuid4()),
                author=user.full_name,
                content=form.content.data,
                created_at=datetime.now(timezone.utc).isoformat(),
                likes=0,
                comments=[],
                liked_by=set()
            )
            save_post(new_post)
            flash("Your post was published successfully.")
        else:
            flash("Post cannot be empty.")
        return redirect(url_for('blogpage'))

    @app.route('/merchandise')
    def merchandise():
        return render_template("merchandise.html", products=product_list, show_cart=True)

    @app.route('/logout', methods=['POST'])
    def logout():
        session.clear()
        return redirect(url_for('login'))

    @app.route('/resources')
    def resources():
        joke = get_programming_joke()
        return render_template('resources.html', joke=joke)

    @app.errorhandler(401)
    def unauthorized(e):
        return render_template("401.html", show_logo_only=True), 401

    @app.errorhandler(403)
    def forbidden(e):
        return render_template("403.html", show_logo_only=True), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html", show_logo_only=True), 404

    @app.errorhandler(500)
    def internal_error(e):
        return render_template('500.html', show_logo_only=True), 500