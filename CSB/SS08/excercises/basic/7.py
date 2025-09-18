def binarySearch(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


result = binarySearch(
    [int(x) for x in input("Enter sorted numbers separated by spaces: ").split()],
    int(input("Enter the number to search for: ")),
)

print(f"Number found at index: {result}" if result != -1 else "Number not found")
