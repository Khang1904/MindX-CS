names = {}

for x in range(int(input("Enter number of students: "))):
    name, age = input(f"Enter name and age of student {x+1}: ").split()
    names[name] = int(age)

target = input("Enter name to get age: ")
print(names[target] if target in names else "Not found")
