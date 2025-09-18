names = {}

for x in range(int(input("Enter number of students: "))):
    name, age = input(f"Enter name and age of student {x+1}: ").split()
    names[name] = int(age)

name = input("Enter name to update: ")
if name in names:
    names[name] = int(input("Enter new age: "))
else:
    print("Name not found")
print(names)
