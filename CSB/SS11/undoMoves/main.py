def record(stack, move):
    stack.append(move)


def undo(stack):
    if not stack:
        print("No moves to undo.")
        return None
    move = stack.pop()
    print(f"Undid move: {move}")
    return move


if __name__ == "__main__":
    stack = []

    while True:
        print(stack)
        match input("Enter action: "):
            case "record":
                record(stack, input("Enter move: "))
            case "undo":
                undo(stack)
            case "exit":
                exit("Exiting the game.")
            case "help":
                print(
                    """
                    record   Records a move
                    undo     Undos the last move
                    exit     Exits the game
                    """
                )
            case _:
                print("Command not found. Type 'help' for more info.")
        print()
