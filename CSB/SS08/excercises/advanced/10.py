def findNearest(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    candidates = []
    if left < len(arr):
        candidates.append(arr[left])
    if right >= 0:
        candidates.append(arr[right])
    return min(candidates, key=lambda x: abs(x - target)) if candidates else None


print(
    "Closest number:",
    findNearest(
        [int(x) for x in input("Enter sorted numbers: ").split()],
        int(input("Enter target number: ")),
    ),
)
