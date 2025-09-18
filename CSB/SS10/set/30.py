ls = list(map(int, input("Enter list of numbers: ").split()))
result = []
for i in range(len(ls)):
    for j in range(len(ls)):
        if i != j and ls[i] % ls[j] == 0:
            result.append(ls[i])
            break
print(result)
