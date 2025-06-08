class BankAccount:
    def __init__(self, balance=0):
        if balance<0:
            raise ValueError("Bank Balance cannot be zero")
        self.balance=balance
    def deposit(self,amount):
        if amount<=0:
            raise ValueError("amount must be positive")
        self.balance+=amount
    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError("Amount cannot be negative")   
        self.balance-=amount
        