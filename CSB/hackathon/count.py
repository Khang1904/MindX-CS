from math import floor

stdin = list(map(int, input("Enter nums: ").split()))

n = floor(len(stdin) / 3)
count = {}

for i in stdin:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

stdout = []

for k, v in count.items():
    if v > n:
        stdout.append(k)

print(stdout)
