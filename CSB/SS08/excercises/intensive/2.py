def selectionSort(arr):
    compares = 0
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            compares += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr, compares


arr, compares = selectionSort(
    [int(i) for i in input("Enter numbers separated by spaces: ").split()]
)

print("Sorted array is: ", arr)
print("Number of comparisons: ", compares)
