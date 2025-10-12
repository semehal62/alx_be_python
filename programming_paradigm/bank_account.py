class  BankAccount:
    def __init__(self,account_balance = 0 ):
        self.account_balance = account_balance
    Implement , withdraw(amount), and display_balance() methods
    def deposit(self,amount):
        self.amount = amount
        self.account_balance += amount
        print(f"Deposited: ${amount}")
    def withdraw(self,amount):
        self.amount = amount
        if ( self.account_balance >= amount):
            print(f"Withdrew: ${amount}")
            return True
        else:
            print("Insufficient funds.")
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
       
