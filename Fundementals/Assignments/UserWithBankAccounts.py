class BankAccount:
    
    
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self,int_rate, balance): 
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
        print(f"\n Balance {self.balance}")
        return self

    def yield_interest(self):
        if self.balance >= 0:
            self.balance+=self.int_Rate
        return self

    def  transfer_money(self, amount,user):
        self.balance-=amount
        user.account.balance+=amount

    @classmethod
    def BankAccount_summary(cls):
        sum = 0
        for account in cls.all_accounts:
            sum=account
            print(f"\n Balance: {sum}")
        return sum


# We can now access the BankAccount class through our self.account attribute
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def deposit(self,amount):
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
        print(f"\n Balance {self.balance}")
        return self

    def  transfer_money(self, amount,user):
        self.account.balance-=amount
        user.account.balance+=amount

Mike = User('Mike','MikeL@codingdojo.com')
Mike.account.deposit(50)
Mike.account.display_account_info()

Sara = User('Sara','SaraB@codingdojo.com')
Sara.account.deposit(10)
Sara.account.display_account_info()

# Money transfer
Mike.account.transfer_money(5,Sara)
Mike.account.display_account_info()

Sara.account.display_account_info()