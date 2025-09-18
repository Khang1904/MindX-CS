names = [{}, {}]

for i in range(2):
    for x in range(int(input(f"Enter number of students in list {i+1}: "))):
        name, age = input(f"Enter name and age of student {x+1}: ").split()
        names[i][name] = int(age)
    print()

combined = names[0]

for name, age in names[1].items():
    combined[name] = age

print(combined)
