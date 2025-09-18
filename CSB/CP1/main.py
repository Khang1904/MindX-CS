from statistics import mean
import warnings


class Student:
    def __init__(self, name, grades=None):
        self.name = name
        if grades is None:
            self.grades = []
        else:
            self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        return mean(self.grades)


class GradeManager:
    def __init__(self, students=None):
        if students is None:
            self.students = {}
        else:
            self.students = students

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)
            print(f"Student {name} added.")
        else:
            warnings.warn(f"Student {name} already exists.", stacklevel=2)

    def record_grade(self, name, grade):
        if name in self.students:
            self.students[name].add_grade(grade)
            print(f"Grade {grade} recorded for {name}.")
        else:
            warnings.warn(f"Student {name} not found.", stacklevel=2)

    def calculate_average_all(self):
        if not self.students:
            return 0
        total_average = mean(
            student.calculate_average() for student in self.students.values()
        )
        return total_average

    def save_data(self, filename):
        with open(filename, "w") as file:
            for student in self.students.values():
                file.write(f"{student.name}: {student.calculate_average()}\n")


grade_manager = GradeManager()

while True:
    print(
        """
    1. Add Student
    2. Record Grade
    3. Calculate Average for All Students
    4. Save Data
    5. Exit
    """
    )
    option = input("Choose an option: ")

    match option:
        case "1":
            name = input("Enter student name: ")
            grade_manager.add_student(name)
        case "2":
            name = input("Enter student name: ")
            grade = float(input("Enter grade: "))
            grade_manager.record_grade(name, grade)
        case "3":
            average = grade_manager.calculate_average_all()
            print(f"Average grade for all students: {average}")
        case "4":
            filename = input("Enter filename to save data: ")
            grade_manager.save_data(filename)
            print(f"Data saved to {filename}.")
        case "5":
            exit("Exiting the program.")
        case _:
            print("Invalid option. Please try again.")
