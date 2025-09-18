def bubbleSort(arr):
    swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, swaps


result, swaps = bubbleSort(
    [
        int(x)
        for x in input("Enter the elements of the array separated by space: ").split()
    ]
)

print("Sorted array:", result)
print("Number of swaps:", swaps)
