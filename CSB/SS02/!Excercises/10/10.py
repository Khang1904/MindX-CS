try:
    stdin = input("Enter numbers: ")
    numbers = list(map(int, stdin.split()))
except ValueError:
    exit("Error: Non-integer value found in the input.")


def checkPrime(num):
    if num < 2:
        return 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == False:
            return False
    return True


count = 0

for number in numbers:
    if checkPrime(number):
        count += 1

print(f"There are {count} prime numbers.")
