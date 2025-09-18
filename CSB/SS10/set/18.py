stdin = list(map(int, input("Enter set of numbers: ").split()))
for i in stdin:
    if i % 3 != 0:
        stdin.remove(i)
print(stdin)
