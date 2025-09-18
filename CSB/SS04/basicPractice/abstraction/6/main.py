from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print("*beep*")
        print(f"Paid {amount} using Credit Card.\n")


class Cash(PaymentMethod):
    def pay(self, amount):
        print("*cash register sound*")
        print(f"Paid {amount} using Cash.\n")


class BankTransfer(PaymentMethod):
    def pay(self, amount):
        print("*bank transfer sound*")
        print(f"Paid {amount} using Bank Transfer.\n")


customers = [CreditCard(), Cash(), BankTransfer()]

for customer in customers:
    customer.pay(100.0)
