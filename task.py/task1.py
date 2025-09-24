class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("insufficient")    
    def get_balance(self):
            print(self.balance)      

b_acc = BankAccount("alan",200) 
b_acc.deposit(700)
b_acc.withdraw(1000)
b_acc.get_balance()
 
