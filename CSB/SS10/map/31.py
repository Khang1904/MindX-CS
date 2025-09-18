k, v = input("Enter names: ").split(), input("Enter ages: ").split()

print(dict(zip(k, map(int, v))))
