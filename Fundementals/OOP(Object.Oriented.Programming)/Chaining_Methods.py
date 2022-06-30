class User:
    Bank_Account = "Credit Union"
    def __init__(self,name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance+=amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance-=amount
        return self

    def  transfer_money(self, amount,user):
        self.account_balance-=amount
        user.account_balance+=amount

    def display_user_balance(self):
        print(f" User: {self.name}, Balance: {self.account_balance}")
        return self
    

women = User("Helen")
women.make_deposit(50).make_deposit(100).make_deposit(25).make_withdrawal(-50).display_user_balance()

male = User("Bob")
male.make_deposit(400).make_withdrawal(1000).make_withdrawal(-200).make_withdrawal(-80).display_user_balance()

teen = User("Sara")
teen.make_deposit(500).make_withdrawal(20).make_withdrawal(100).make_withdrawal(60).display_user_balance()

women.transfer_money(50,teen)
women.display_user_balance()

teen.display_user_balance()