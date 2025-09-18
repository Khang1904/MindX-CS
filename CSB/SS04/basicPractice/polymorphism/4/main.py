class Person:
    def greet(self):
        print("Hello, I am a person.")
        print("I have no special traits.")


class Student:
    def greet(self):
        print("I am also a student.")
        print("I study hard and aim for good grades.")


class Teacher:
    def greet(self):
        print("I am a teacher.")
        print("I love sharing knowledge and guiding students.")


people = [Person(), Student(), Teacher()]
for person in people:
    person.greet()
    print()  # Print a newline for better readability
