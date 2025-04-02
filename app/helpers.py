import shelve
import uuid
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data') #typo in previous version. Fixed. KR 02/04/2025

#ensure the data directory exists - KR 02/04/2025
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

USERS_DB = os.path.join(DATA_DIR, 'users.db')
POSTS_DB = os.path.join(DATA_DIR, 'posts.db')

# USER FUNCTIONS
def load_users():
    """Load users as a list"""
    with shelve.open(USERS_DB) as db:
        return list(db.values())

def get_user(email):
    """Load a user by their email"""
    with shelve.open(USERS_DB) as db:
        return db.get(email)
    
def save_user(user):
    """save a user by their email as a key"""
    with shelve.open(USERS_DB, writeback=True) as db:
        db[user['email']] = user

#POST FUNCTIONS
def load_posts():
    """Load all posts as a list"""
    with shelve.open(POSTS_DB) as db:
        return sorted(db.values(), key=lambda p: p.get('created_at', ''), reverse=True)
   

def save_post(new_post):
    """This will save a post using a UUID if not already present"""
    with shelve.open(POSTS_DB, writeback=True) as db:
        if 'id' not in new_post:
            new_post['id'] = str(uuid.uuid4())
        db[new_post['id']] = new_post

def find_post_by_id(post_id):
    """Find a post by its ID"""
    with shelve.open(POSTS_DB) as db:
        return db.get(post_id)
    
def update_post(post_id, updated_post):
    """Update a post by its ID"""
    with shelve.open(POSTS_DB, writeback=True) as db:
        if post_id in db:
            db[post_id].update(updated_post)
            db[post_id] = updated_post

def delete_post(post_id):
    """Delete a post by its ID"""
    with shelve.open(POSTS_DB, writeback=True) as db:
        if post_id in db:
            del db[post_id]