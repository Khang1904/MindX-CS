print(
    "The two sets intersect."
    if set(input("Enter set one: ").split()) & set(input("Enter set two: ").split())
    else "The two sets don't intersect."
)
