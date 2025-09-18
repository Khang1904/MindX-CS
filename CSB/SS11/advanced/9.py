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

    def forward(self):
        if self.forwardStack:
            self.backStack.append(self.currentPage)
            self.currentPage = self.forwardStack.pop()
        else:
            print("No pages in forward history.")

    def refresh(self):
        if self.currentPage is not None:
            print(f"Refreshing page: {self.currentPage}")
        else:
            print("No page to refresh.")


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
            case "forward":
                browser.forward()
            case "refresh":
                browser.refresh()
            case "exit":
                running = False
            case "help":
                print(
                    """
                    visit      Visit a web page
                    back       Go back
                    forward    Go forward
                    refresh    Refreshes the current page
                    exit       Exits the program
                    """
                )
            case _:
                print("Command not found. Type 'help' for commands.")

        print()

    print("Exiting the program.")
