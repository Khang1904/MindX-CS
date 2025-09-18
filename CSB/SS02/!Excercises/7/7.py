try:
    stdin = input("Enter numbers: ")
    numbers = map(int, stdin.split())
except ValueError:
    exit("Error: Non-integer value found in the input.")

print("Largest number:", max(numbers))
