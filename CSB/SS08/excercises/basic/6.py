def countItem(arr, target):
    count = 0
    for i in arr:
        if i == target:
            count += 1
    return count


result = countItem(
    [int(x) for x in input("Enter numbers separated by spaces: ").split()],
    int(input("Enter the number to count: ")),
)

print("Number found " + str(result) + " times" if result > 0 else "Number not found")
