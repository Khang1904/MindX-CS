class MultiLevelQueue:
    def __init__(self):
        self.data = {"high": [], "low": []}

    def add_high(self, x):
        self.data["high"].append(x)

    def add_low(self, x):
        self.data["low"].append(x)

    def serve(self):
        if len(self.data["high"]) < 1:
            print(self.data["low"].pop(0))
        else:
            print(self.data["high"].pop(0))


if __name__ == "__main__":
    q = MultiLevelQueue()

    while True:
        op = input("Enter a command: ").split()
        match op[0]:
            case "high":
                q.add_high(op[1])
            case "low":
                q.add_low(op[1])
            case "serve":
                q.serve()
            case "exit":
                break
            case _:
                print("Unknown command.")
