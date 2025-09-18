ls = map(int, input("Enter numbers, space-splitted: ").split())
sorted_ls = sorted(ls, reverse=True)
print(sorted_ls[1] if len(sorted_ls) > 1 else None)
