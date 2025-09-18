def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


arr = []

for x in range(int(input("Enter number of arrays: "))):
    arr.extend(
        map(
            int,
            input(f"Enter the elements of array {x+1} separated by space: ").split(),
        )
    )

print("Merged and sorted array:", selectionSort(arr))
