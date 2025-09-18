stdin = input("Enter word: ")
stack = []
reversedStr = ""

for c in stdin:
    stack.append(c)

while stack:
    reversedStr += stack.pop()

print(reversedStr)
