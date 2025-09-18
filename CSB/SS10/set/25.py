seen = []
dupes = []

n = list(map(int, input("Enter list of numbers").split()))

for x in n:
    if x in seen:
        dupes.append(x)
    else:
        seen.append(x)

print("Unique elements are:", [x for x in seen if x not in dupes])
