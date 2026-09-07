class TextEditor:

    def __init__(self):

        # Undo stack...
        self.undo_stack = []

        # Redo stack...
        self.redo_stack = []

        # Current document....
        self.document = ""


    def make_change(self, new_txt):

        # Save current document in undo stack...
        self.undo_stack.append(self.document)

        # Update the document...
        self.document = new_txt

        # Clear old redo history...
        self.redo_stack.clear()

        print("Changes made successfully.")


    def undo(self):

        # Check if there is anything to undo...
        if not self.undo_stack:
            print("Nothing to undo.")
            return

        # Save current document in redo stack...
        self.redo_stack.append(self.document)

        # Restore previous document....
        self.document = self.undo_stack.pop()

        print("Undo task performed.")


    def redo(self):

        # Check if there is anything to redo...
        if not self.redo_stack:
            print("Nothing to redo.")
            return

        # Save current document in undo stack...
        self.undo_stack.append(self.document)

        # Restore document from redo stack....
        self.document = self.redo_stack.pop()

        print("Redo performed successfully.")


    def display_document(self):

        print("\nCurrent Document:")
        print(self.document)


editor = TextEditor()


while True:

    print("\n===== TEXT EDITOR =====")
    print("1. Make a Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":

        new_text = input("Enter the new document text: ")
        editor.make_change(new_text)


    elif choice == "2":

        editor.undo()


    elif choice == "3":

        editor.redo()


    elif choice == "4":

        editor.display_document()


    elif choice == "5":

        print("Exiting text editor...")
        break


    else:

        print("Invalid choice. Please try again.")
