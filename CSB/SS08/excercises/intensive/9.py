def find_left(arr, target):
    left, right = 0, len(arr) - 1
    res = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res


def find_right(arr, target):
    left, right = 0, len(arr) - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res


arr = list(map(int, input("Enter numbers separated by space: ").split()))
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

l = find_left(arr, lower)
r = find_right(arr, upper)

if l <= r:
    print("Values in range:", arr[l : r + 1])
else:
    print("No values in the given range.")
