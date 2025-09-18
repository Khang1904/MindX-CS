def getNum():
    valid = False

    while not valid:
        try:
            num = int(input("Enter a number: "))
            valid = True
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return num


def oddSum(num):
    oddSum = 0

    for i in range(1, num + 1, 2):
        oddSum += i

    print(f"Sum of odd numbers from 1 to {num} is: {oddSum}")


def checkPrime(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def findFactors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    print(f"Factors of {num} are: {', '.join(map(str, factors))}")


num = getNum()
oddSum(num)
if checkPrime(num) == True:
    print(f"{num} is prime.")

else:
    print(f"{num} is not prime.")
    findFactors(num)
