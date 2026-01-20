# tests/test_notes.py

import unittest
import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.file_ops import NOTES_FILE, init_storage, load_notes, save_notes

class TestNotesManager(unittest.TestCase):

    def setUp(self):
        if os.path.exists(NOTES_FILE):
            os.remove(NOTES_FILE)
        init_storage()

    def test_add_and_load_notes(self):
        notes = [{"title": "Test Note", "content": "This is a test"}]
        save_notes(notes)
        loaded = load_notes()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["title"], "Test Note")

    def test_empty_storage(self):
        notes = load_notes()
        self.assertEqual(notes, [])

    def test_multiple_notes(self):
        notes = [
            {"title": "Note1", "content": "Content1"},
            {"title": "Note2", "content": "Content2"}
        ]
        save_notes(notes)
        loaded = load_notes()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[1]["title"], "Note2")

    def tearDown(self):
        if os.path.exists(NOTES_FILE):
            os.remove(NOTES_FILE)

if __name__ == "__main__":
    unittest.main()
