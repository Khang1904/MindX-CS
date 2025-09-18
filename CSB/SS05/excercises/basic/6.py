def countValues(ls, value):
    count = 0
    for item in ls:
        if item == value:
            count += 1
    return count


print(
    countValues(
        map(int, input("Enter the list of numbers (space-separated): ").split()),
        int(input("Enter the value to count: ")),
    ),
    "times",
)
