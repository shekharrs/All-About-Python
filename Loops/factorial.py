# Factorial in Python

# n = int(input("Enter a number: "))

# res = 1
# for i in range(2, n+1) :       
#     res = res * i
# print("factorial is", + res)    

###############################################

# Using Library Function
import math

n = int(input("Enter a number: "))
res = math.factorial(n)
print("factorial is", +res)