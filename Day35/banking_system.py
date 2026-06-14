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

class SavingsAccount(Account):
    def __init__(self, acc_number, owner, balance=0, min_balance=500, interest_rate=0.04):
        super().__init__(acc_number, owner, balance)
        self.min_balance = min_balance
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            super().withdraw(amount)
        else:
            print(f"Cannot withdraw ₹{amount}. Minimum balance of ₹{self.min_balance} must be maintained.")

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Interest added ₹{interest:.2f}, Balance: ₹{self.balance:.2f}")
        print(f"Interest of ₹{interest:.2f} added. New balance: ₹{self.balance:.2f}")

class CurrentAccount(Account):
    def __init__(self, acc_number, owner, balance=0, overdraft_limit=10000):
        super().__init__(acc_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            self.transactions.append(f"Withdrew ₹{amount} (Overdraft allowed), Balance: ₹{self.balance}")
            print(f"₹{amount} withdrawn. New balance: ₹{self.balance}")
        else:
            print("Withdrawal exceeds overdraft limit!")

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, acc_number, owner, acc_type="savings"):
        if acc_number not in self.accounts:
            if acc_type == "savings":
                self.accounts[acc_number] = SavingsAccount(acc_number, owner)
            elif acc_type == "current":
                self.accounts[acc_number] = CurrentAccount(acc_number, owner)
            print(f"{acc_type.capitalize()} Account {acc_number} created for {owner}.")
        else:
            print("Account number already exists!")

    def get_account(self, acc_number):
        return self.accounts.get(acc_number, None)