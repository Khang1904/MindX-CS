q = input("Enter list of customers: ").split(",")

for _ in range(int(input("Enter number of customers to serve: "))):
    print("Served:", q.pop(0))

print("Remaining:", q)
