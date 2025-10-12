class  BankAccount:
    def __init__(self ,account_balance = 0 ):
        self.account_balance = account_balance
    
    def deposit(self,amount):
        self.amount = amount
        self.account_balance += amount
       
    def withdraw(self,amount):
        self.amount = amount
        if ( self.account_balance >= amount):
            self.account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        acc = f "self.account_balance :.2f"
        print(f"Current Balance: ${acc}")
       
