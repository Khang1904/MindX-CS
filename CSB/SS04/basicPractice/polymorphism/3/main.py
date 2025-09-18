class Shape:
    def describe(self):
        pass


class Circle(Shape):
    def describe(self):
        print("This is a circle.")
        print("It has no corners and is round.")


class Square(Shape):
    def describe(self):
        print("This is a square.")
        print("It has four equal sides and four corners.")


class Triangle(Shape):
    def describe(self):
        print("This is a triangle.")
        print("It has three sides and three corners.")


shapes = [Circle(), Square(), Triangle()]

for shape in shapes:
    shape.describe()
    print()  # Print a newline for better readability
