k, v = input("Enter names: ").split(), input("Enter scores: ").split()
v = list(map(int, v))


print(dict(zip(k, v)))
print("Average score:", sum(v) / len(v))
