from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class PDF(Printable):
    def print(self):
        return "Printing PDF document."


class Word(Printable):
    def print(self):
        return "Printing Word document."


class Image(Printable):
    def print(self):
        return "Printing Image document."


files = [PDF(), Word(), Image()]

for file in files:
    print(file.print())
