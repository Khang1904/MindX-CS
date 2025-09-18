from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Transport):
    def move(self):
        return "The car is driving on the road."


class Bicycle(Transport):
    def move(self):
        return "The bicycle is pedaling on the path."


class Bus(Transport):
    def move(self):
        return "The bus is transporting passengers on the route."


vehicles = [Car(), Bicycle(), Bus()]

for vehicle in vehicles:
    print(vehicle.move())
