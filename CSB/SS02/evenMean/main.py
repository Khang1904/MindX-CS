from statistics import mean

stdin = input("Enter a list of numbers separated by spaces: ")

try:
    numbers = map(int, stdin.split())
    even_numbers = [num for num in numbers if num % 2 == 0]
except ValueError:
    exit("Invalid input. Please enter a list of integers.")

if even_numbers:
    even_mean = mean(even_numbers)
    print(f"The mean of the even numbers: {even_mean}")
else:
    print("No even numbers found in the input.")
