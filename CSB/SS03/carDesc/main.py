class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def describe(self):
        return f"The {self.color} car has {self.mileage} miles."


blueCar = Car("blue", 20000)
redCar = Car("red", 30000)

print(blueCar.describe())
print(redCar.describe())
