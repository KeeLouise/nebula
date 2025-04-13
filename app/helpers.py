import shelve, uuid, os, requests
import dbm.dumb
from datetime import datetime, timezone

# Wrapper to force shelve to use dbm.dumb backend – Render workaround. KR 13/04/2025
class DumbShelf(shelve.Shelf):
    def __init__(self, filename, flag='c', protocol=None, writeback=False):
        db = dbm.dumb.open(filename, flag)
        super().__init__(db, protocol=protocol, writeback=writeback)

# Define path to data folder – KR 02/04/2025
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')  # typo in previous version. Fixed. KR 02/04/2025

# Ensure the data directory exists – KR 02/04/2025
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Define file paths for shelve databases – note: no .db extension for dbm.dumb
USERS_DB = os.path.join(DATA_DIR, 'users_shelve')
POSTS_DB = os.path.join(DATA_DIR, 'posts_shelve')


# USER FUNCTIONS
def load_users():
    """Load users as a list"""
    with DumbShelf(USERS_DB) as db:
        return list(db.values())

def get_user(email):
    """Load a user by their email"""
    with DumbShelf(USERS_DB) as db:
        return db.get(email)

def save_user(user):
    """Save a user using their email as the key"""
    with DumbShelf(USERS_DB, writeback=True) as db:
        db[user['email']] = user

# POST FUNCTIONS
def load_posts():
    """Load all posts as a list, sorted by created_at descending"""
    with DumbShelf(POSTS_DB) as db:
        return sorted(db.values(), key=lambda p: p.get('created_at', ''), reverse=True)

def save_post(new_post):
    """Save a post using a UUID if not already present"""
    with DumbShelf(POSTS_DB, writeback=True) as db:
        if 'id' not in new_post:
            new_post['id'] = str(uuid.uuid4())
        if 'created_at' not in new_post:
            new_post['created_at'] = datetime.now(timezone.utc).isoformat()
        db[new_post['id']] = new_post

def save_posts(posts):
    """Overwrite all posts"""
    with DumbShelf(POSTS_DB, writeback=True) as db:
        db.clear()
        for post in posts:
            db[post['id']] = post

def find_post_by_id(post_id):
    """Find a post by its ID"""
    with DumbShelf(POSTS_DB) as db:
        return db.get(post_id)

def update_post(post_id, updated_post):
    """Update a post by its ID"""
    with DumbShelf(POSTS_DB, writeback=True) as db:
        if post_id in db:
            db[post_id].update(updated_post)
            db[post_id] = updated_post

def delete_post(post_id):
    """Delete a post by its ID"""
    with DumbShelf(POSTS_DB, writeback=True) as db:
        if post_id in db:
            del db[post_id]


# REST API for Programming Jokes
def get_programming_joke():
    url = "https://v2.jokeapi.dev/joke/Programming?safe-mode"
    res = requests.get(url)
    data = res.json()
    return data