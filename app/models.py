import json

def load_users():
    with open('users.json') as f:
        return json.load(f)