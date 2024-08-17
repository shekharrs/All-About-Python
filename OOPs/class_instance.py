# Class and Instance🔥

class Employee:
    compName = "gfg"        # class attribute
    def __init__(self, id):
        self.id = id        # instance attribute

e = Employee(1001)
print(e.compName)
print(e.id)
print(Employee.compName)
