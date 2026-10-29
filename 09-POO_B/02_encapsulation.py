class BankAccount:
    
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
    def to_string(self):
        str_show = f'[balance: {self.__balance}]'
        return str_show

account = BankAccount(1000)
print(account.to_string())
account.deposit(500)
print(account.to_string())