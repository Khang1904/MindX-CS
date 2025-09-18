def sortAndSearch(arr, target):
    # Sort the array
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    # Perform binary search
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr, mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return arr, -1


arr, result = sortAndSearch(
    [int(x) for x in input("Enter numbers separated by spaces: ").split()],
    int(input("Enter the number to search for: ")),
)

print("Sorted array:", arr)
print(
    f"Index of the target number is {result}"
    if result != -1
    else "Target number not found"
)
