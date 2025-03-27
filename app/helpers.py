import json
import os

def load_users():
    users_file = os.path.join(os.path.dirname(__file__), 'data', 'users.json')
    try:
        with open(users_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_users(users):
    users_file = os.path.join(os.path.dirname(__file__), 'data', 'users.json')
    with open(users_file, 'w') as f:
        json.dump(users, f, indent=2)
