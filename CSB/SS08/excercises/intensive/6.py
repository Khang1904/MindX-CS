def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


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


arr = []

for x in range(int(input("Enter number of arrays: "))):
    arr.extend(
        map(
            int,
            input(f"Enter the elements of array {x+1} separated by space: ").split(),
        )
    )

target = int(input("Enter the target value to search for: "))

sortedArray = selectionSort(arr)

print("Merged and sorted array:", sortedArray)
print("Index of target value:", binarySearch(sortedArray, target))
