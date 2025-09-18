names = {}

for x in range(int(input("Enter number of students: "))):
    name, age = input(f"Enter name and age of student {x+1}: ").split()
    names[name] = int(age)

name = input("Enter name to search: ")
if name in names:
    print(names[name])
else:
    print("Name not found")
