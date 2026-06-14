class Account:
    def __init__(self, acc_number, owner, balance=0):
        self.acc_number = acc_number
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}, Balance: ₹{self.balance}")
        print(f"₹{amount} deposited. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew ₹{amount}, Balance: ₹{self.balance}")
            print(f"₹{amount} withdrawn. New balance: ₹{self.balance}")
        else:
            self.transactions.append(f"Failed withdrawal ₹{amount}, Balance: ₹{self.balance}")
            print("Insufficient balance!")

    def show_balance(self):
        print(f"Account {self.acc_number} balance: ₹{self.balance}")

    def show_transactions(self):
        print(f"Transaction history for Account {self.acc_number}:")
        for t in self.transactions:
            print("-", t)