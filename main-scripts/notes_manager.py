# main-scripts/notes_manager

from utils.file_ops import init_storage, load_notes, save_notes

# Add a new note
def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")

    notes = load_notes()

    # Prevent duplicate titles
    for note in notes:
        if note["title"].lower() == title.lower():
            print("A note with this title already exists. Try another title.")
            return

    notes.append({"title": title, "content": content})
    save_notes(notes)
    print(f"Note '{title}' added successfully!")

# View all notes
def view_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return

    print("\n--- All Notes ---")
    for idx, note in enumerate(notes, start=1):
        print(f"{idx}. {note['title']} - {note['content']}")

# Search notes by keyword
def search_notes():
    keyword = input("Enter keyword to search: ").lower()
    notes = load_notes()
    found = [note for note in notes if keyword in note["title"].lower() or keyword in note["content"].lower()]

    if not found:
        print("No matching notes found.")
    else:
        print("\n--- Search Results ---")
        for idx, note in enumerate(found, start=1):
            print(f"{idx}. {note['title']} - {note['content']}")

# Delete a note by title
def delete_note():
    title = input("Enter the title of the note to delete: ")
    notes = load_notes()
    updated_notes = [note for note in notes if note["title"].lower() != title.lower()]

    if len(updated_notes) == len(notes):
        print(f"No note found with title '{title}'.")
    else:
        save_notes(updated_notes)
        print(f"Note '{title}' deleted successfully!")

# Menu system
def main():
    init_storage()
    while True:
        print("\n--- Personal Notes Manager ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
