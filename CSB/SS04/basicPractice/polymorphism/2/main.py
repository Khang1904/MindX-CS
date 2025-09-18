class Add:
    def operate(self, a, b):
        return a + b


class Subtract:
    def operate(self, a, b):
        return a - b


class Multiply:
    def operate(self, a, b):
        return a * b


class Divide:
    def operate(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


x = Add().operate(5, 3)
y = Subtract().operate(5, 3)
z = Multiply().operate(5, 3)
w = Divide().operate(5, 3)
