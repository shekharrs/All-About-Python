# Class and Objects in Python🔥

# class: blueprint
# object: instance

# class complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#     def print(self):
#         print(str(self.real)+"+i"+str(self.imag))
#     def add(self, c):
#         self.real += c.real
#         self.imag += c.imag

# c1 = complex(10,20)
# c1.print()
# c2 = complex(20,30)
# c1.add(c2)
# c1.print()

#############################################################################

# Real life use case of class & objects

class Student:

    # default constructor
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding Student Details in the Database..")

s1 = Student("Rohan", 98)  
print(s1.name, s1.marks) # Rohan 98

s2 = Student("Mohan", 88)
print(s2.name, s2.marks) # Mohan 88
