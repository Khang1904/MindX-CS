from abc import ABC, abstractmethod


class Question(ABC):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    @abstractmethod
    def ask(self):
        pass

    @abstractmethod
    def check_answer(self, user_answer):
        pass


class MCQ(Question):
    def __init__(self, question, answer, options):
        super().__init__(question, answer)
        self.options = options

    def ask(self):
        print(self.question)
        for i, option in enumerate(self.options):
            print(f"{chr(65+i)}. {option}")

    def check_answer(self, user_answer):
        return user_answer.upper() == self.answer


class TrueFalse(Question):
    def __init__(self, question, answer):
        super().__init__(question, answer)

    def ask(self):
        print(self.question)
        print("True")
        print("False")

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer


class Essay(Question):
    def __init__(self, question, answer):
        super().__init__(question, answer)

    def ask(self):
        print(self.question)

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()


quiz = [
    MCQ("What is the capital of France?", "B", ["Berlin", "Paris", "Madrid", "Rome"]),
    TrueFalse("The Earth is flat.", "false"),
    Essay(
        "Explain the theory of relativity.",
        "Einstein's theory that describes the relationship between space and time.",
    ),
]

for question in quiz:
    question.ask()
    user_answer = input("Your answer: ")
    if question.check_answer(user_answer):
        print("Correct!\n")
    else:
        print(f"Incorrect! The correct answer is: {question.answer}\n")
