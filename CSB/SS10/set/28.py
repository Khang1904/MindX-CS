ls = list(map(int, input("Enter list of numbers: ").split()))

result = []
for i in ls:
    if not result:
        result.append(i)
    elif i != result[-1]:
        result.append(i)
print(result)
