seen = set()
seenTwice = set()

for c in input("Enter a string: "):
    if c not in seen and c not in seenTwice:
        seen.add(c)
    else:
        seenTwice.add(c)
        seen.discard(c)

print("Characters seen once:", seen)
