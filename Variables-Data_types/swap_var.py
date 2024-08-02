# Swapping two variables🤖

# Using extra variables to swap
student_one = 'python'
student_two = 'dsa'

temp_name = student_one
student_one = student_two
student_two = temp_name
print(student_one)
print(student_two)


# Using comma assignment
block_1 = 10
block_2 = 20

block_1,block_2 = block_2,block_1
print(block_1)
print(block_2)


# Using comma to assign multi values to multi variables
x, y ,z = 100, "python", 10.5
print(x)
print(y)
print(z)

x,y = x-5,y+"learning"  
print(x)
print(y)