def findGreatestBelowThreshold(numbers, threshold):
    greatest = None
    for number in numbers:
        if number < threshold:
            if greatest is None or number > greatest:
                greatest = number
    return greatest


print(
    "Greatest number below threshold:",
    findGreatestBelowThreshold(
        [int(x) for x in input("Enter numbers separated by spaces: ").split()],
        int(input("Enter threshold: ")),
    ),
)
