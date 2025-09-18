a = set(list(input("Enter first word: ")))
b = set(list(input("Enter second word: ")))
print(a | b - a & b)
