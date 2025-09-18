def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
        return -1
    return -1


print(linear_search([1, 2, 3, 4, 5], 3))
