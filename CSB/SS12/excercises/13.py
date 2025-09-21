class PriorityQueue:
    def __init__(self):
        self.data = {}

    def insert(self, v, p):
        if p not in self.data:
            self.data[p] = []
        self.data[p].append(v)

    def remove(self):
        keys = list(self.data.keys())
        highestPriority = max(keys)
        print(self.data[highestPriority].pop(0))
        to_delete = [k for k in keys if len(self.data[k]) == 0]
        for k in to_delete:
            del self.data[k]


if __name__ == "__main__":
    q = PriorityQueue()

    while True:
        op = input(">>>").split()
        match op[0]:
            case "insert":
                q.insert(op[1], int(op[2]))
            case "remove":
                q.remove()
            case "exit":
                break
            case _:
                print("Unknown command. Availble commands: insert <v> <p>, remove")
