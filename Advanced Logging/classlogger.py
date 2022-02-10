import logging

classLogger = logging.getLogger(__name__)
classLogger.setLevel(logging.INFO)

classFormat = logging.Formatter("%(levelname)s:%(filename)s --> %(message)s")
classHandler = logging.FileHandler("./Advanced Logging/class.log")
classHandler.setFormatter(classFormat)

classLogger.addHandler(classHandler)


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        classLogger.info(f"Created Employee: {self.fullname} --> {self.email}")

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com".lower()

    @property
    def fullname(self):
        return f"{self.first} {self.last}"


emp1 = Employee("John", "Doe")
emp2 = Employee("Jane", "Doe")
