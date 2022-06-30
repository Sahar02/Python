class BankAccount:
    
    
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_Rate = 0.01
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance-=amount
        else:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance-=2
        return self

    def display_account_info(self):
        print(f"Balance {self.balance}")
        return self

    def yield_interest(self):
        if self.balance >= 0:
            self.balance+=self.int_Rate
        return self

    @classmethod
    def BankAccount_summary(cls):
        sum = 0
        for account in cls.all_accounts:
            sum+=account.balance
            print(f"Balance: {sum}")
        return sum

person1 = BankAccount(0,0)
person2 = BankAccount(50,0)

person1.deposit(50).deposit(50).deposit(50).withdraw(200).yield_interest().display_account_info()
person2.deposit(200).deposit(50).withdraw(80).withdraw(90).withdraw(100).yield_interest().display_account_info()