# Class member access🔥
'''
Python, similarly to other object-oriented allows the user to write short and beautiful code by enabling the developer to define classes to create objects.

The developer can define the prototype of an object class based on two types of members:

Instance members: Instance variables in python are such that when defined in the parent class of the object are instantiated and separately maintained for each and every object instance of the class. These are usually called using the self. Keyword. The self keyword is used to represent an instance of the class.

Class members: Class members may be defined in the scope of the class. These may usually be used with the cls keyword. The cls keyword is similar to the self keyword but unlike the self keyword, it represents the class itself.
Class variables can be declared in the class outside the methods without using any keyword. 

'''

"""
class Student:
    college_name = "XYZ University"       # class 

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def wlcm(self):
        print(f"Congratulation {s1.name} for brilliant performance in your final year")

    def get_marks(self):
        return self.marks                 # instance              

s1 = Student("Bill Gates", 98)
print(f"The name of the student is {s1.name}, and the marks obtained are {s1.marks}%")
s1.wlcm()
print(s1.get_marks())

"""


# we define the following class with a instance variable  
class Node: 
  cls_msg = "This is stored in an class variable."
  def __init__(self): 
      
    # this is a instance variable 
    self.msg = "This is stored in an instance variable." 
  
  
print(Node.cls_msg) 
print(Node().cls_msg)
print(Node.self.msg())