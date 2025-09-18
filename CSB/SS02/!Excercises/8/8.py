from statistics import mean

# Collect numbers divisible by 5 in a list
numbers_div5 = []

try:
    stdin = input("Enter numbers: ")
    numbers = list(map(int, stdin.split()))
except ValueError:
    exit("Error: Non-integer value found in the input.")

for number in numbers:
    if number % 5 == 0:
        numbers_div5.append(number)

if numbers_div5:
    print("Mean of numbers divisible by 5:", mean(numbers_div5))
else:
    print("No numbers divisible by 5 found.")
