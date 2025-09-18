from statistics import median
import os

if not os.path.exists("data.txt"):
    exit("Error: data.txt file does not exist.")

with open("data.txt", "r") as file:
    lines = file.read().split()
    try:
        numbers = [int(line.strip()) for line in lines]
    except ValueError:
        exit("Error: Non-integer value found in the file.")

if not numbers:
    exit("Error: No numbers found in the file.")

print("Median:", median(numbers))
