n = int(input("Enter a number: "))

stack = []

while n:
    stack.append(str(n % 2))
    n //= 2

binary = ""

while stack:
    binary += stack.pop()

print(binary)
