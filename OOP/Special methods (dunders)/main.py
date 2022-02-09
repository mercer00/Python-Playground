#=========================================================================================#
#=========================================================================================#
#=========================================================================================#

"""
special methods
special methods are also called dunder methods as they are surrounded by double underscores
dunder init is the most useful special method used in classes
there is also dunder repr and dunder str
dunder str and dunder repr are run when the instance of a class is printed
dunder str is more user friendly reply while dunder repr should be something for developers and something that can be used in the code itself.
if both dunder str and repr are present , dunder str is run when the instance is printed and if str is missing and repr is present , repr is run
we can also run these specifically by using str(instance) and repr(instance)

there are also many other dunder methods that we use very often such as add , mul , len , etc

for example , 

print(1+2) is the same as print(int.__add__(1 , 2))
print("a"+"b") is the same as print(str.__add__("a" , "b"))
print(len("sus")) is the same as print("sus".__len__())

We can add these methods to our classes to our methods in order to define a functionality for when we need to add , sub or use sum other operator between our instances

All dunder methods inside a class basically look like this:

__dunder__(self , other)

self and other are the two instances that the property is run on

"""
#=========================================================================================#
#=========================================================================================#
#=========================================================================================#


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def __repr__(self):
        return f"Employee(\"{self.first}\", \"{self.last}\", {self.pay})"

    def __str__(self):
        return f"{self.fullname()} --> {self.pay}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee("Scooby", "Doo", 50000)
print(emp1)
print(repr(emp1))
print(str(emp1))

emp2 = Employee("Snoopy", "Doo", 100000)
print(emp2)

print(emp1 + emp2)
print(len(emp1))
print(len(emp2))
