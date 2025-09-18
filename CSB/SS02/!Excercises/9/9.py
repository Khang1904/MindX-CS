from statistics import mean, median, multimode

try:
    stdin = input("Enter numbers: ")
    numbers = list(map(int, stdin.split()))
except ValueError:
    exit("Error: Non-integer value found in the input.")

with open("report.txt", "w") as file:
    if numbers:
        file.write(f"Report on the set of numbers: {numbers}\n")
        file.write(f"Mean: {mean(numbers)}\n")
        file.write(f"Median: {median(numbers)}\n")
        file.write(f"Mode: {multimode(numbers)}\n")
    else:
        print("No numbers provided.\n")
