stdin = list(map(int, input("Enter set of numbers: ").split()))
result = [i for i in stdin if (i % 2 == 0) and (i % 3 == 0)]
print(result)
