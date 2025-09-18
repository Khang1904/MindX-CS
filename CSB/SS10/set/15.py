n = list(map(int, input("Enter list of numbers").split()))

seen = set()
dupes = set()
for x in n:
    if x in seen:
        dupes.add(x)
    else:
        seen.add(x)
print("Unique elements are:", seen - dupes)
