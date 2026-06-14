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
    
# Menu-driven program
def main():
    bank = Bank("MyBank")

    while True:
        print("\n--- Banking Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Show Balance")
        print("5. Show Transactions")
        print("6. Add Interest (Savings only)")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            acc_number = input("Enter account number: ")
            owner = input("Enter owner name: ")
            acc_type = input("Enter account type (savings/current): ").lower()
            bank.create_account(acc_number, owner, acc_type)

        elif choice == "2":
            acc_number = input("Enter account number: ")
            account = bank.get_account(acc_number)
            if account:
                amount = int(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("Account not found!")

        elif choice == "3":
            acc_number = input("Enter account number: ")
            account = bank.get_account(acc_number)
            if account:
                amount = int(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("Account not found!")

        elif choice == "4":
            acc_number = input("Enter account number: ")
            account = bank.get_account(acc_number)
            if account:
                account.show_balance()
            else:
                print("Account not found!")

        elif choice == "5":
            acc_number = input("Enter account number: ")
            account = bank.get_account(acc_number)
            if account:
                account.show_transactions()
            else:
                print("Account not found!")

        elif choice == "6":
            acc_number = input("Enter account number: ")
            account = bank.get_account(acc_number)
            if isinstance(account, SavingsAccount):
                account.add_interest()
            else:
                print("Interest can only be added to Savings Accounts.")

        elif choice == "7":
            print("Exiting... Thank you for banking with us!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()