"""
Animal
    |-- Dog
    |-- Cat
    |-- Duck
"""


class Animal:
    def speak(self):
        print("Random noises.")


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


class Duck(Animal):
    def speak(self):
        print("Quack!")


animals = [Animal(), Dog(), Cat(), Duck()]

for animal in animals:
    animal.speak()
