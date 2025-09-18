def bubbleSort(arr):
    if not arr:
        return arr
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


stdin = input("Enter numbers separated by spaces: ").split()
nums = [int(num) for num in stdin]
sorted_nums = bubbleSort(nums)
print("Sorted numbers:", sorted_nums)
