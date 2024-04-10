"""
Напишите класс BankAccount, имеющий следующие свойства и методы:

- __init__(self, balance): конструктор, принимающий начальный баланс счета
- balance: свойство, которое возвращает текущий баланс счета
- deposit(self, amount): метод, который позволяет внести деньги на счет
- withdraw(self, amount): метод, который позволяет снять деньги со счета
- close(self): метод, который закрывает счет и возвращает оставшиеся на нем деньги

Для свойства balance используйте декоратор @property.
"""


class BankAccount:
    def __init__(self, balance):
        self.balance = balance


    @property
    def _balance(self):
        return self.balance


    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if amount > self._balance:
            print("не достаточно денег!")
        else:
            self.balance -= amount


    def close(self):
        not_money = self.balance
        self.balance = 0
        return not_money


# код для проверки 
account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit(500)
print(account.balance)  # 1500

account.withdraw(200)
print(account.balance)  # 1300

account.close()
print(account.balance)  # 0
