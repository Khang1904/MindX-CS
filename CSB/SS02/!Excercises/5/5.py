def filterEven(numbers):
    return [num for num in numbers if num % 2 == 0]


try:
    stdin = input("Enter numbers: ")
    numbers = map(int, stdin.split())
except ValueError:
    exit("Error: Non-integer value found in the input.")

print("Even numbers:", end=" ")
print(*filterEven(numbers), sep=", ")
