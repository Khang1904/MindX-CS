print(
    list(
        set([int(i) for i in input("Enter first list of numbers: ").split()])
        & set([int(i) for i in input("Enter second list of numbers: ").split()])
    )
)
