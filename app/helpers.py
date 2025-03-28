import json
import os

def get_users_file():
    """Returns the correct path to the users.json file"""
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    users_file = os.path.join(data_dir, 'users.json')

    # Ensure the data directory exists - KR 27/03/2025
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Ensure users.json exists - KR 27/03/2025
    if not os.path.exists(users_file):
        with open(users_file, 'w') as f:
            json.dump([], f)  # Initialize with an empty list if users.json does not exist - KR 27/03/2025

    return users_file

def load_users():
    """Load users from users.json file"""
    users_file = get_users_file()
    try:
        with open(users_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_users(users):
    """Save users to users.json file"""
    users_file = get_users_file()
    with open(users_file, 'w') as f:
        json.dump(users, f, indent=2)

def save_user(new_user):
    """Append a new user to users.json"""
    users = load_users()
    users.append(new_user)
    save_users(users)    #Updated code to append a new user to users.json - KR 28/03/2025

def get_posts_file():
    """Returns the correct path to the posts.json file"""
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    posts_file = os.path.join(data_dir, 'posts.json')

    # Ensure the data directory exists - kr 28/03/2025
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Ensure posts.json exists - KR 28/03/2025
    if not os.path.exists(posts_file):
        with open(posts_file, 'w') as f:
            json.dump([], f)

    return posts_file

def load_posts():
    """Load posts from posts.json file"""
    posts_file = get_posts_file()
    try:
        with open(posts_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_posts(posts):
    """Save posts to posts.json file"""
    posts_file = get_posts_file()
    with open(posts_file, 'w') as f:
        json.dump(posts, f, indent=2)

def save_post(new_post):
    posts = load_posts()
    posts.insert(0, new_post)  # inserts new post at the beginning of the list - KR 28/03/2025
    save_posts(posts)