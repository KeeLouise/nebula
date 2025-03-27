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
