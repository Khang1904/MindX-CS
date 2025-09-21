class CircularQueue:
    def __init__(self, c):
        self.data = []
        self.cap = c

    def enqueue(self, x):
        if len(self.data) == self.cap:
            print("Queue full.")
            return
        self.data.append(x)

    def dequeue(self):
        if len(self.data) == 0:
            print("Nothing to dequeue.")
            return
        return self.data.pop(0)


if __name__ == "__main__":
    q = CircularQueue(int(input("Enter size of queue: ")))
    while True:
        op = input(">>> ").split()
        match op[0]:
            case "enqueue":
                q.enqueue(op[1])
            case "dequeue":
                q.dequeue()
            case "exit":
                break
            case _:
                print("Unknown command. Use 'enqueue' or 'dequeue'.")
        print(q.data)
