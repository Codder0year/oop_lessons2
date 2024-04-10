def printing(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func} result {result}')
        return result

    return inner





@printing
def add_one(x):
    return x+1

# new_f = printing(add_one)
# x = new_f(10)

x = add_one(19)
print(x)




import random
def integer(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        result_int = int(result)
        return result_int

    return inner

@integer
def get_random_nubmer():
    return random.randint(1, 100) / random.randint(1, 100)
print(get_random_nubmer())




import datetime

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Jon', 'Snow', 50000)
emp_2 = Employee('Ivan', 'Ivanov', 60000)
print(Employee.raise_amt)
Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'Jon-Snow-70000'
emp_str_2 = 'Ivan-Ivanov-30000'
emp_str_3 = 'Elena-Nikitina-90000'

first, last, pay = emp_str_1.split('-')
#new_emp_1 = Employee(first, last, pay)

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)


my_date = datetime.date(2023, 1, 31)
print(Employee.is_workday(my_date))