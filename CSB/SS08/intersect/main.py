def intersect(a, b):
    result = []
    for i in a:
        for j in b:
            if i == j and i not in result:
                result.append(i)
    return result


print(
    "The intersection of the two lists is:",
    intersect(
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
