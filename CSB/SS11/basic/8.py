stdin = input("Enter equation: ")

stack = []
pairs = {")": "(", "}": "{", "]": "["}

valid = True

for c in stdin:
    if c in "{[(":
        stack.append(c)
    elif c in "}])":
        if not stack or stack[-1] != pairs[c]:
            valid = False
            break
        stack.pop()

valid = not stack

print("Equation valid" if valid else "Equation invalid")
