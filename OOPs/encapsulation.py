# Encapsulation --> (hidden)
# Access Modifier --> encapsulation
# Access Modifier --> private, protected, public

# Private  (to keep internal functionality hidden that is why we use private variable)
"""
class Person:
    # constructor
    def __init__(self, name, age):
        self.__name = name      # Private --> (double underscore)
        self.__age = age

    def display_info(self):
        print(f"The person name is {self.__name} and the age is {self.__age}")

personDetails = Person("Bill Gates", 99)
personDetails.display_info()    
"""


# Protected
"""
class Person:
    # constructor
    def __init__(self, name, age):
        self._name = name        # Protected --> (Single underscore)
        self._age = age

person = Person("Sam", 98)

dir(person)
person._age

class Student(Person):
    # constructor
    def __init__(self, name, age):
        super().__init__(name, age)

    def display_info(self):
        print(f"The person name is {self._name} and the age is {self._age}")

student1 = Student("Mark", 18)
student1.display_info() 
"""           


# Public
class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"The Student name is {self.name} and the age is {self.age}")

studentInfo = Person("Messi", 23)            
studentInfo.display_info()