print(
    "Set A is a subset of Set B"
    if set([int(i) for i in input("Enter set A: ")]).issubset(
        set([int(i) for i in input("Enter set B: ")])
    )
    else "Set A is not a subset of Set B"
)
