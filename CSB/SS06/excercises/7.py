# Imports
from random import sample, choice, randint
from time import time


# Search Algorithms
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


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


# Test Data Generation
testcase = sample(range(100000), 1000)
target = choice(testcase) if randint(0, 1) != 0 else randint(0, 1000)
sorted_testcase = sorted(testcase)

# Search Execution and Timing
time_start = time()
linear_result = linear_search(testcase, target)
linear_time = time() - time_start

time_start = time()
binary_result = binary_search(sorted_testcase, target)
binary_time = time() - time_start

# Result Comparison
result = (
    "Linear Search is faster"
    if linear_time < binary_time
    else (
        "Binary Search is faster"
        if binary_time < linear_time
        else "Both searches took the same time"
    )
)

# Print all outputs at the end
print("Testcase:", testcase, "\n")
print("Target:", target, "\n")
print(linear_result)
print("Linear Search Time:", linear_time, "\n")
print(binary_result)
print("Binary Search Time:", binary_time, "\n")
print(result)
