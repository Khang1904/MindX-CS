class WordProcessor:
    def __init__(self):
        self.currentText = ""
        self.undoStack = []
        self.redoStack = []

    def edit(self, new_text):
        self.undoStack.append(self.currentText)
        self.currentText = new_text
        self.redoStack.clear()

    def undo(self):
        if self.undoStack:
            self.redoStack.append(self.currentText)
            self.currentText = self.undoStack.pop()
        else:
            print("Nothing to undo.")

    def redo(self):
        if self.redoStack:
            self.undoStack.append(self.currentText)
            self.currentText = self.redoStack.pop()
        else:
            print("Nothing to redo.")


if __name__ == "__main__":
    wp = WordProcessor()
    running = True

    print("Welcome to Python Word Processor!\n")

    while running:
        match input("Enter an action: "):
            case "edit":
                print("Enter new document text (end with a single '.' on a line):")
                lines = []
                while True:
                    line = input()
                    if line.strip() == ".":
                        break
                    lines.append(line)
                wp.edit("\n".join(lines))
            case "undo":
                wp.undo()
            case "redo":
                wp.redo()
            case "exit":
                running = False
            case _:
                print("Command not found. Available commands: edit, undo, redo, exit.")

        print()

    print("Exiting the program.")
