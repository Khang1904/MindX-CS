def charCount(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


print(charCount(input("Enter a string: ")))
