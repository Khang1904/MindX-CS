def sortAndSearch(arr, target):
    # Sort the array
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Perform linear search
    for index, value in enumerate(arr):
        if value == target:
            return arr, index
    return arr, -1


arr, result = sortAndSearch(
    [int(x) for x in input("Enter numbers separated by space: ").split()],
    int(input("Enter the number to search for: ")),
)

print("Sorted array:", arr)
print(
    f"Index of the target number is {result}"
    if result != -1
    else "Target number not found"
)
