import shelve, uuid, os, requests
import dbm.dumb
from datetime import datetime, timezone

# Wrapper to force shelve to use dbm.dumb backend – Render workaround. KR 13/04/2025
class DumbShelf(shelve.Shelf):
    def __init__(self, filename, flag='c', protocol=None, writeback=False):
        db = dbm.dumb.open(filename, flag)
        super().__init__(db, protocol=protocol, writeback=writeback)

# Define path to data folder – KR 02/04/2025
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# Ensure the data directory exists – KR 02/04/2025
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Define file paths for shelve databases – no .db extension
USERS_DB = os.path.join(DATA_DIR, 'users_shelve')
POSTS_DB = os.path.join(DATA_DIR, 'posts_shelve')

# CLASS DEFINITIONS - KR 13/04/2025
class User:
    def __init__(self, full_name, email, password):
        self.full_name = full_name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "email": self.email,
            "password": self.password
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            full_name=data.get("full_name"),
            email=data.get("email"),
            password=data.get("password")
        )

class Post:
    def __init__(self, id, author, content, created_at, likes=0, comments=None, liked_by=None):
        self.id = id
        self.author = author
        self.content = content
        self.created_at = created_at
        self.likes = likes
        self.comments = comments or []
        self.liked_by = set(liked_by) if liked_by else set()

    def to_dict(self):
        return {
            "id": self.id,
            "author": self.author,
            "content": self.content,
            "created_at": self.created_at,
            "likes": self.likes,
            "comments": self.comments,
            "liked_by": list(self.liked_by)
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            author=data.get("author"),
            content=data.get("content"),
            created_at=data.get("created_at"),
            likes=data.get("likes", 0),
            comments=data.get("comments", []),
            liked_by=data.get("liked_by", [])
        )

# USER FUNCTIONS
def load_users():
    """Load users as User objects"""
    with DumbShelf(USERS_DB) as db:
        return [User.from_dict(u) for u in db.values()]

def get_user(email):
    """Load a User by email"""
    with DumbShelf(USERS_DB) as db:
        data = db.get(email)
        return User.from_dict(data) if data else None

def save_user(user):
    """Save a User object"""
    with DumbShelf(USERS_DB, writeback=True) as db:
        db[user.email] = user.to_dict()

# POST FUNCTIONS
def load_posts():
    """Load all posts as Post objects, sorted newest first"""
    with DumbShelf(POSTS_DB) as db:
        posts = [Post.from_dict(p) for p in db.values()]
        return sorted(posts, key=lambda p: p.created_at or '', reverse=True)

def save_post(post):
    """Save a Post object"""
    with DumbShelf(POSTS_DB, writeback=True) as db:
        if not post.id:
            post.id = str(uuid.uuid4())
        if not post.created_at:
            post.created_at = datetime.now(timezone.utc).isoformat()
        db[post.id] = post.to_dict()

def save_posts(posts):
    """Overwrite all posts with a list of Post objects"""
    with DumbShelf(POSTS_DB, writeback=True) as db:
        db.clear()
        for post in posts:
            db[post.id] = post.to_dict()

def find_post_by_id(post_id):
    """Return a single Post object by ID"""
    with DumbShelf(POSTS_DB) as db:
        data = db.get(post_id)
        return Post.from_dict(data) if data else None

def update_post(post_id, updated_post):
    """Update a post by its ID with a Post object"""
    with DumbShelf(POSTS_DB, writeback=True) as db:
        if post_id in db:
            db[post_id] = updated_post.to_dict()

def delete_post(post_id):
    """Delete a post by ID"""
    with DumbShelf(POSTS_DB, writeback=True) as db:
        if post_id in db:
            del db[post_id]

def time_ago(iso_str):
    try:
        created_at = datetime.fromisoformat(iso_str)
    except Exception:
        return "some time ago"

    now = datetime.now(timezone.utc)
    diff = now - created_at

    seconds = diff.total_seconds()
    minutes = int(seconds // 60)
    hours = int(minutes // 60)
    days = int(hours // 24)

    if seconds < 60:
        return "just now"
    elif minutes < 60:
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    elif hours < 24:
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    elif days < 7:
        return f"{days} day{'s' if days != 1 else ''} ago"
    else:
        return created_at.strftime('%b %d, %Y')  # fallback to full date - KR 16/04/2025
    
# Programming Joke API
def get_programming_joke():
    url = "https://v2.jokeapi.dev/joke/Programming?safe-mode"

    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        data = res.json()

        if data.get("type") == "single":
            return data.get("joke")
        elif data.get("type") == "twopart":
            return f"{data.get('setup')} — {data.get('delivery')}"
        else:
            return "We tried to find a joke, but it got lost in the code..."

    except Exception as e:
        return "Oops! Our joke server is having a bad day. Try again later."