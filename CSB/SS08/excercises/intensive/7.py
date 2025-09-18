def linearFindClosest(numbers, target):
    if not numbers:
        return None

    closest = numbers[0]
    min_diff = abs(closest - target)

    for number in numbers:
        diff = abs(number - target)
        if diff < min_diff:
            min_diff = diff
            closest = number

    return closest


print(
    "Closest value to target is:",
    linearFindClosest(
        [int(x) for x in input("Enter numbers separated by space: ").split()],
        int(input("Enter target number: ")),
    ),
)
