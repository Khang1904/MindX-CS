def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def linearSum(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs if pairs else None


arr = bubbleSort(list(map(int, input("Enter numbers separated by space: ").split())))
tar = int(input("Enter target sum: "))

print("Sorted array:", arr)
print("Pairs with sum", tar, ":", linearSum(arr, tar))
