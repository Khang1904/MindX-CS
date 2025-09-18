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

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest: {interest}. New balance: {self.balance}")


def main():
    account = Account("135", "John Smith", 2500)
    savesAccount = SavingsAccount("123", "John Doe", 1000, 0.05)

    account.withdraw(500)

    savesAccount.deposit(200)
    savesAccount.apply_interest()

    print(f"Account balance: {account.getBalance()}")
    print(f"Savings account balance: {savesAccount.getBalance()}")


main()
