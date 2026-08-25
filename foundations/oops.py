class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount} . New balance : {self.balance}")
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:    
            self.balance = self.balance - amount
            print(f"Withdrew {amount} . New balance : {self.balance}")
    def show_balance(self):
        print(f"owner: {self.owner}, balance: {self.balance}")
# Create an account
acc = BankAccount("SND", 1000)

# Use the account
acc.show_balance()
acc.deposit(500)
acc.withdraw(2000)
acc.show_balance()