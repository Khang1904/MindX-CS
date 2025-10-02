def enqueue_action(queue, action):
    queue.append(action)


def dequeue_action(queue):
    return queue.pop(0)


queue = []

while True:
    action = input("Enter an action (or 'print' to start printing): ")
    if action == "print":
        break

    enqueue_action(queue, action)

while queue:
    print(f'Printing: "{dequeue_action(queue)}"')
