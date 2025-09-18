a = set(input("Enter Math club members: ").split())
b = set(input("Enter IT club members: ").split())

print(
    "Members of one club:",
    (a | b) - (a & b),
)
