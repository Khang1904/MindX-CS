class Rectangle:
    def area(self, w, h):
        print(w * h)


class Circle:
    def area(self, r):
        print(3.14 * r * r)


class Triangle:
    def area(self, b, h):
        print(0.5 * b * h)


shapes = [Rectangle(), Circle(), Triangle()]

shapes[0].area(5, 10)  # Rectangle area
shapes[1].area(7)  # Circle area
shapes[2].area(6, 8)  # Triangle area
