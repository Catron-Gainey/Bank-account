class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
        return self
        
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        else:
            self.balance = self.balance - amount
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
        return self

account1 = BankAccount(.01, 500)
account1.deposit(500).deposit(500).deposit(500).withdraw(300).yield_interest().display_account_info()

account2 = BankAccount(.01, 1000)
account2.deposit(1000).deposit(1000).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()
