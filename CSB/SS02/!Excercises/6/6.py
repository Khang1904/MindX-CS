def positiveSum(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total


try:
    stdin = input("Enter numbers: ")
    numbers = map(int, stdin.split())
except ValueError:
    exit("Error: Non-integer value found in the input.")

print("Sum of positives:", end=" ")
print(positiveSum(numbers), sep=", ")
