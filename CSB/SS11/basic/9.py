class Browser:
    def __init__(self):
        self.currentPage = None
        self.backStack = []
        self.forwardStack = []

    def visit(self, url):
        if self.currentPage is not None:
            self.backStack.append(self.currentPage)
        self.currentPage = url
        self.forwardStack.clear()  # Clear forward history on new visit

    def back(self):
        if self.backStack:
            self.forwardStack.append(self.currentPage)
            self.currentPage = self.backStack.pop()
        else:
            print("No pages in back history.")


if __name__ == "__main__":
    browser = Browser()
    running = True

    print("Welcome to Python Browser!\n")

    while running:
        if browser.currentPage:
            print("Current page:", browser.currentPage)
        match input("Enter an action: "):
            case "visit":
                browser.visit(input("Enter URL: "))
            case "back":
                browser.back()
            case "exit":
                running = False
            case "help":
                print(
                    """
                    visit      Visit a web page
                    back       Go back
                    exit       Exits the program
                    """
                )
            case _:
                print("Command not found. Type 'help' for commands.")

        print()

    print("Exiting the program.")
