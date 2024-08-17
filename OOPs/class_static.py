# Class methods and Static methods🔥

# Class methods : Allow operations related to the class itself
# take (cls) as the first parameter, which represents the class itself.

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of student: {cls.count}"
    
    @classmethod
    def get_total_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa:{cls.total_gpa // cls.count}"

student1 = Student("Driwk", 3.45)
student2 = Student("Bruce", 4.02)
student3 = Student("Sam", 2.78)

print(Student.get_count())
print(Student.get_total_gpa())