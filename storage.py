import json

FILE_NAME = "members.json"

def load_members():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_members(members):
    with open(FILE_NAME, "w") as file:
        json.dump(members, file, indent=4)
