def insertionSort(arr):
    # Standard insertion sort (in-place)
    arr = arr.copy()  # Work on a copy to avoid modifying input
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


stdin = input("Enter numbers separated by spaces: ").split()
nums = [int(num) for num in stdin]
sorted_nums = insertionSort(nums)
print("Sorted numbers:", sorted_nums)
