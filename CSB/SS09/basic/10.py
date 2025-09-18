def countGrade(ls):
    grade_count = {"A": 0, "B": 0, "C": 0, "D": 0}

    for grade in ls:
        match grade:
            case x if x >= 9:
                grade_count["A"] += 1
            case x if x >= 7:
                grade_count["B"] += 1
            case x if x >= 5:
                grade_count["C"] += 1
            case x if x < 5:
                grade_count["D"] += 1

    return grade_count


print(
    "Grade counts:",
    countGrade([int(x) for x in input("Enter scores separated by space: ").split()]),
)
