ls = list(map(int, input("Enter list of numbers: ").split()))
s = set(ls)
d = dict.fromkeys(s, 0)
for i in ls:
    d[i] += 1
print(d)
