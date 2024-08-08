# Find First Digit Number in Python

# Method 1 
# def getFirstDigit(x):
#     while x >= 10:
#         x = x//10
#     return x
# x = int(input("Enter a number: "))
# print(getFirstDigit(x))

######################################################

# Method 2

from math import log10

def getFirstDigit(x):
    d = int(log10(x))

    res = x // (10 ** d)

    return res
x = int(input("Enter x: "))
print(getFirstDigit(x))