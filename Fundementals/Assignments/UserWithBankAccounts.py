class BankAccount:
    
    
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_Rate =int_rate
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
            sum+=account
            print(f"Balance: {sum}")
        return sum


class User(BankAccount):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.01, balance=0)

    def deposit(self, amount):
        self.account+=amount
        return self

    def withdraw(self, amount):
        if amount < self.account:
            self.account-=amount
        else:
            print(f"Insufficient funds: Charging a $5 fee")
            self.account-=2
        return self

    def display_account_info(self):
        print(f"\nBalance {self.account}")
        return self