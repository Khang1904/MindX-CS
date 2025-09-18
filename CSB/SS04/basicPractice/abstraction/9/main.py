from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def work(self):
        pass


class Student(Person):
    def work(self):
        print("Studying for exams")


class Teacher(Person):
    def work(self):
        print("Teaching students")


people = [Student(), Teacher()]
for person in people:
    person.work()
