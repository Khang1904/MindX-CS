class Account:
    def __init__(self, number, name, balance):
        self.number = number
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, number, name, balance, interest_rate):
        super().__init__(number, name, balance)
        self.interest_rate = interest_rate
