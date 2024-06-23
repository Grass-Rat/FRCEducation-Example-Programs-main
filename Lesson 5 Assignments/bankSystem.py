class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} into account {self.account_number}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount} from account {self.account_number}. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance}")

account = BankAccount("1234567890", "John Doe")
account.check_balance()
account.deposit(1000)
account.withdraw(500)
account.check_balance()