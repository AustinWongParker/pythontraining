'''
OOP Practice in Python using Bank Accounts

Austin Wong-Parker

6 - 11 - 19

** All code is written by me for PRACTICE only **
'''

class BankAccount:
    def __init__(self):
        self.balance = 90

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def getBalance(self):
        return self.balance


a = BankAccount()
b = BankAccount()

a.deposit(2000)
b.deposit(500)
a.withdraw(899)
d = b.withdraw(399)

c = a.getBalance()

print('Total for bank account A: ' + str(a.balance))
print('Total for bank account B: ' + str(b.balance))
print('Total for A: ' + str(c) + ' B: ' + str(d))
