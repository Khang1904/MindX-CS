def linear_search(arr, target):
    indexes = []
    for i, v in enumerate(arr):
        if v == target:
            indexes.append(i)
    return indexes if indexes else []


print(
    "Indexes of target in array: ",
    linear_search(
        [int(i) for i in input("Enter array elements separated by space: ").split()],
        int(input("Enter target value: ")),
    ),
)
