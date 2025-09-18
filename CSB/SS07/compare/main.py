from time import time
from random import sample, choice, randint


def insertionSort(arr):
    # Standard insertion sort (in-place)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bubbleSort(arr):
    if not arr:
        return arr
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Test Data Generation
testcase = sample(range(100000), 1000)
target = choice(testcase) if randint(0, 1) != 0 else randint(0, 1000)

# Search Execution and Timing
time_start = time()
insertion_result = insertionSort(testcase.copy())
insertion_time = time() - time_start

time_start = time()
bubble_result = bubbleSort(testcase.copy())
bubble_time = time() - time_start

# Result Comparison
if insertion_time < bubble_time:
    result = "Insertion Sort is faster"
elif insertion_time > bubble_time:
    result = "Bubble Sort is faster"
else:
    result = "Both sorts are equally fast"

# Print all outputs at the end
print("Testcase:", testcase, "\n")
print("Target:", target, "\n")
print(insertion_result)
print("Linear Search Time:", insertion_time, "\n")
print(bubble_result)
print("Binary Search Time:", bubble_time, "\n")
print(result)
