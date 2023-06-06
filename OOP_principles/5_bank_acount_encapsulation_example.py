# Define a class representing a bank account
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds.")
    
    def get_balance(self):
        return self._balance

# Create an instance of the BankAccount class
account = BankAccount("123456789", 1000)

# Perform deposit, withdrawal, and check balance
account.deposit(500)
account.withdraw(200)
print(account.get_balance())
