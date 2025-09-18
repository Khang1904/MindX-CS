def binarySearchAll(arr, target):
    left, right = 0, len(arr) - 1
    occurences = 0

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            occurences += 1
            for i in range(mid - 1, -1, -1):
                if arr[i] == target:
                    occurences += 1
                else:
                    break

            for i in range(mid + 1, len(arr)):
                if arr[i] == target:
                    occurences += 1
                else:
                    break

            return occurences
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0


print(
    "Number of occurrences of target:",
    binarySearchAll(
        [
            int(i)
            for i in input("Enter sorted array elements separated by space: ").split()
        ],
        int(input("Enter target element: ")),
    ),
)
