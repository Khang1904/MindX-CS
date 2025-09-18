# def checkDuplicates(ls):
#     for i in range(len(ls)):
#         for j in range(i + 1, len(ls)):
#             if ls[i] == ls[j]:
#                 return True


def checkDuplicates(ls):
    seen = set()
    for item in ls:
        if item in seen:
            return True
        seen.add(item)
    return False


list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5, 1]

print(checkDuplicates(list1))
print(checkDuplicates(list2))
