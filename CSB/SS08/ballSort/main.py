def ballSort(balls):
    order = ["red", "white", "blue"]
    colors = {}
    for ball in balls:
        if ball not in colors:
            colors[ball] = 0
        colors[ball] += 1

    sorted_balls = []
    for color in order:
        if color in colors:
            sorted_balls.extend([color] * colors[color])
    return sorted_balls


print(
    "The sorted ball list is:",
    ballSort(
        [
            x.strip()
            for x in input("Enter the list of balls separated by space: ").split()
        ]
    ),
)
