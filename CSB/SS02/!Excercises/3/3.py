import os

if not os.path.exists("data.txt"):
    exit("File data.txt does not exist.")

stdin = input("Enter numbers: ")
numbers = map(int, stdin.split())

with open("data.txt", "w") as file:
    for n in numbers:
        if n % 2 != 0:
            file.write(f"{n}\n")
