class Stack:
    # 🔮 Magic Methods
    def __init__(self, *data):
        self.data = list(data) if data else []

    def __repr__(self):
        return repr(self.data)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    # 📦 Stack Operations
    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def isEmpty(self):
        return not self.data

    def size(self):
        return len(self.data)


s = Stack()

if __name__ == "__main__":
    print("Stack CLI. Commands: push, pop, top, show, exit")
    while True:
        cmd = input("> ").strip().lower()
        match cmd:
            case "push":
                s.push(input("Value: "))
            case "pop":
                print(s.pop() if not s.isEmpty() else "Stack empty")
            case "top":
                print(s[-1] if not s.isEmpty() else "Stack empty")
            case "show":
                print(s)
            case "exit":
                break
            case _:
                print("push, pop, top, show, exit")
