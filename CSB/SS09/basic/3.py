print(
    "Members of both clubs:",
    set(input("Enter Math club members: ").split())
    & set(input("Enter IT club members: ").split()),
)
