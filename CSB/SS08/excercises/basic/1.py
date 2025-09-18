def mergeAndSort(a, b):
    if not a:
        return b
    if not b:
        return a

    merged = a + b
    for i in range(len(merged)):
        for j in range(i + 1, len(merged)):
            if merged[i] > merged[j]:
                merged[i], merged[j] = merged[j], merged[i]

    return merged


print(
    "Merged and sorted list: ",
    mergeAndSort(
        [
            int(x)
            for x in input("Enter first list of numbers separated by space: ").split()
        ],
        [
            int(x)
            for x in input("Enter second list of numbers separated by space: ").split()
        ],
    ),
)
print("Complexity: O(n^2)")
