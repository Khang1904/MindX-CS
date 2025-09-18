def bubbleSortLen(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(arr[j]) < len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(
    "Sorted array by length:",
    bubbleSortLen(
        [x.strip() for x in input("Enter space-separated strings: ").split()]
    ),
)
