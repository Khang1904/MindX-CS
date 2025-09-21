stdin = list(input("Enter word:"))

s1 = stdin.copy()
s2 = []

while s1:
    s2.append(s1.pop())

print(stdin == s2)
