class TwoStackQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if self.out_stack:
            print(self.out_stack.pop())
        else:
            print("Queue is empty.")


if __name__ == "__main__":
    queue = TwoStackQueue()

    for l in range(int(input("Enter number of commands: "))):
        op = input(f"[line {l+1}] ").split()
        match op[0]:
            case "enqueue":
                queue.enqueue(op[1])
            case "dequeue":
                queue.dequeue()
