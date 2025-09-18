names = {}

for x in range(int(input("Enter number of students: "))):
    name, age = input(f"Enter name and age of student {x+1}: ").split()
    names[name] = int(age)

min_age = min(names.values())
for n, a in names.items():
    if a == min_age:
        print(f"The youngest student is {n}.")
        break
