# utils/file_ops.py

import json
import os

# Path to notes file inside main-scripts
NOTES_FILE = os.path.join("main-scripts", "notes_storage.json")

def init_storage():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            json.dump([], f)

def load_notes():
    with open(NOTES_FILE, "r") as f:
        return json.load(f)

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)
