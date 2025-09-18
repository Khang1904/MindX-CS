def linearSearch(s, ch):
    indexes = []
    for index, value in enumerate(s):
        if value == ch:
            indexes.append(index)
    return indexes


result = linearSearch(
    input("Enter a string: "), input("Enter a character to search for: ").strip()
)

print(
    f"Character found at index: {result}"
    if result
    else "Character not found in the string."
)
