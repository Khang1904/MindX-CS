stdin = list(map(int, input("Enter list of numbers: ").split()))
for i in stdin:
    if i % 2 != 0:
        stdin.remove(i)
print(stdin)
