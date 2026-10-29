class BankAccount:
    
    interest_rate = 0.02
    
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
    
    @classmethod # Como es un classmethod cambiara la tasa de interes a nivel de clase y para todas las instancias
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        return True
    
    @staticmethod
    def validate_amount(amount):
        return amount > 0
    
    def withdraw(self, amount):
        if self.validate_amount(amount):
            if self.balance >= amount:
                self.balance -= amount
                return True
            return False
        return False
    

account_one = BankAccount('Camilo', 5000000)
account_two = BankAccount('Aguilar', 0)

print(BankAccount.interest_rate)

interest_rate = BankAccount.change_interest_rate(0.03)

if interest_rate: print('El interes cambio')
print(BankAccount.interest_rate)

def widhdraw(account: BankAccount, amount: int):
    actual_widhdraw = account.withdraw(amount)
    if actual_widhdraw:
        print('El retiro fue exitoso')
    else:
        print('Se presento un problema durante el retiro')

widhdraw(account_one, 50000)
widhdraw(account_two, 50000)