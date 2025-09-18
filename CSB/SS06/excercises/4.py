def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


ls = map(int, input("Enter sorted numbers separated by space: ").strip().split())
tar = int(input("Enter the number to search for: ").strip())
print(f"The index of {tar} is {binary_search(list(ls), tar)}")
