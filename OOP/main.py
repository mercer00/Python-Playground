from calendar import week, weekday
import datetime


class Employee:
    # class variables
    raise_amt = 1.04
    num_of_emps = 0
    # instance variables are defined inside an init method, each time a new instance is created , the init method runs

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first + "." + last + "@company.com").lower()
        Employee.num_of_emps += 1

    # instance methods
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # class methods
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, str):
        first, last, pay = str.split("-")
        return cls(first, last, pay)

    # static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            print("Is a weekday")
        else:
            print("Is not a weekday")


# creating an instance of the class "Employee"
emp1 = Employee("Sushant", "Singh", 50000)
emp2 = Employee("Samarth", "Sharma", 50000)
print(emp1.pay)
print(emp1.email)
print(emp2.pay)
print(emp2.email)
# we need to put a parenthesis here as fullname is a method not an attribute
print(emp1.fullname())
print(emp2.fullname())

emp1.apply_raise()
print(emp1.pay)
print(emp2.pay)

print(Employee.raise_amt)

Employee.set_raise_amt(1.05)

emp1.raise_amt = 1.06
print(emp1.raise_amt)
print(emp2.raise_amt)

new_emp1 = "Scooby-Doo-90000"
emp3 = Employee.from_string(new_emp1)
print(emp3.fullname())
print(emp3.email)
print(emp3.pay)

today_date = datetime.date.today()
another_date = datetime.date(2022, 2, 6)
Employee.is_workday(today_date)
Employee.is_workday(another_date)

print(Employee.num_of_emps)
