'''Encapsulation:-
->Hides internal details, exposing only what’s necessary.
->Achieved using methods and sometimes private variables
(_var or __var).'''
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
