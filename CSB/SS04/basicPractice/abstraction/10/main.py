from abc import ABC, abstractmethod


class Excercise(ABC):
    @abstractmethod
    def showQ(self):
        pass

    @abstractmethod
    def showA(self):
        pass


class MathExcercise(Excercise):
    def showQ(self):
        return "What is 2 + 2?"

    def showA(self):
        return "The answer is 4."


class EnglishExcercise(Excercise):
    def showQ(self):
        return "What is the synonym of 'happy'?"

    def showA(self):
        return "The answer is 'joyful'."


excercises = [MathExcercise(), EnglishExcercise()]
for excercise in excercises:
    print(excercise.showQ())
    print(excercise.showA())
    print()  # Print a newline for better readability
