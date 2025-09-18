def linearSearch(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1


result = linearSearch(
    [int(x) for x in input("Enter numbers separated by spaces: ").split()],
    int(input("Enter the number to search for: ")),
)


print("Number found at index " + str(result) if result != -1 else "Number not found")
