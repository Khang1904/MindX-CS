print(
    "Number is in set"
    if int(input("Enter a number: ")) in set([int(i) for i in input("Enter a set:")])
    else "Number is not in set"
)
