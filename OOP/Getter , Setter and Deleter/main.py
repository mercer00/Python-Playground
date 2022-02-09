from numpy import full


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com".lower()

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print(f"{self} was fired")
        first = None
        last = None

    # adding str for deleter , not needed
    def __str__(self):
        return f"{self.fullname} --> {self.email}"


emp1 = Employee("Sussy", "Lemon")
print(emp1.fullname)
print(emp1.email)
emp1.first = "Sweet"
print(emp1.fullname)
print(emp1.email)

emp1.fullname = "Sweet Orange"
print(emp1.fullname)
print(emp1.email)

del emp1.fullname
