def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(
    "Sorted array in descending order is: ",
    bubbleSort([int(x) for x in input("Enter numbers separated by spaces: ").split()]),
)
