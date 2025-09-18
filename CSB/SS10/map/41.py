stdin = input("Enter a word: ")
count = {}

for char in stdin:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)
