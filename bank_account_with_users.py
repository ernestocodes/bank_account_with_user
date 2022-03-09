class BankAccount:
    bank_name ='Bank Of Ernesto'
    all_accounts = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.check_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print(f"You cannot withdraw {amount}. You only have {self.balance} ")
        return self

    def display_account_info(self):
        print(f"Current interest rate is: {self.int_rate}. Current balance is {self.balance}.")
        return self

    def yield_interest(self):
        if BankAccount.check_positive(self.balance):
            self.balance += self.balance * self.int_rate
            return self
        else:
            print("You need more money to get interest")
            return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()

    @staticmethod
    def check_positive(balance):
        if (balance) <= 0:
            return False
        else:
            return True

    @staticmethod
    def check_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True


class User:

    def __init__(self, name, int_rate, balance):
        self.name = name
        self.account = BankAccount(int_rate, balance)
        self.accounts = []

    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self

    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def display_user_balance(self):
        print(f"{self.name} has a balance of {self.account.balance}")
        return self

    def make_transfer(self, amount, friend):
        self.account.balance -= amount
        friend.account.balance += amount
        print(f"{self.name} has {self.account.balance} remaining. {friend.name} has {friend.account.balance} remaining.")
        return self


ernesto = BankAccount(.15, 500)
michael = BankAccount(.04, 2000)
ernesto.deposit(20).deposit(120).deposit(300).withdraw(940).yield_interest().display_account_info()
michael.deposit(2000).deposit(500).withdraw(150).withdraw(99).withdraw(200).withdraw(15).yield_interest().display_account_info()

BankAccount.print_all_accounts()