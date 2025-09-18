ls = []

for x in range(int(input("Enter number of lists: "))):
    ls.extend(
        list(
            map(
                int, input(f"Enter elements of list {x+1} separated by space: ").split()
            )
        )
    )

print("Set of lists:", set(ls))
