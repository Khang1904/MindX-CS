stdin = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(
    "There are duplicates in this set."
    if sorted(list(set(stdin))) != sorted(stdin)
    else "There are no duplicates in this set."
)
