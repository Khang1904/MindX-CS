def binary_insert(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


arr = [int(x) for x in input("Enter sorted numbers separated by space: ").split()]
target = int(input("Enter the number to insert: "))
index = binary_insert(arr, target)
print(f"Inserted value should be at index: {index}")
