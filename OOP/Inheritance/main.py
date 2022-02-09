#inheritance in classes

class Employee:
    raise_amt = 1.02
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first + "." + last + "@gmail.com").lower
        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt


class Developer(Employee):
    raise_amt = 1.05

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f"--> {emp.fullname()}")


emp1 = Employee("Scooby", "Doo", 50000)
dev1 = Developer("John", "Smilga", 50000, "JavaScript")

print(emp1.fullname())
print(emp1.raise_amt)
print(dev1.fullname())
print(dev1.raise_amt)

print(dev1.prog_lang)

manager1 = Manager("Snoop", "Dogg", 100000, [emp1])

print(manager1.fullname())
print(manager1.raise_amt)

manager1.add_emp(dev1)
manager1.remove_emp(emp1)
manager1.print_emps()

print(Employee.num_of_emps)
