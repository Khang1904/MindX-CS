stdin = input("Enter path: ").split("/")

path = []

for i in stdin:
    if i == "..":
        if len(path) > 0:
            path.pop()
    elif i == "." or i == "":
        continue
    else:
        path.append(i)

print("/" + "/".join(path))
