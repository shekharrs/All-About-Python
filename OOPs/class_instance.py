# Class and Instance🔥

class Employee:
    compName = "gfg"
    def __init__(self, id):
        self.id = id

e = Employee(1001)
print(e.compName)
print(e.id)
print(Employee.compName)
