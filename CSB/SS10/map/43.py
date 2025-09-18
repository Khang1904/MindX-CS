names = {}

for x in range(int(input("Enter number of students: "))):
    name, age = input(f"Enter name and age of student {x+1}: ").split()
    names[name] = int(age)

max_age = max(names.values())
for n, a in names.items():
    if a == max_age:
        print(f"The oldest student is {n}.")
        break
