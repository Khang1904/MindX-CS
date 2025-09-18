print(
    "Prime numbers are:",
    [
        x
        for x in list(set(map(int, input("Enter list of numbers: ").split())))
        if all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1
    ],
)
