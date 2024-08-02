# Type Conversion - Implicit Conversion & Explicit Conversion🔥
"""
Implicit conversion: Python automatically converts one data type to another without any user involvement. 
This is done to avoid data loss or type errors

Explicit conversion: The user manually converts the data type of an object using built-in functions. 
This is also called typecasting
"""

# Implicit Conversion
a=10
b=1.5
c=a+b  # a convert to float
print(c)

d=True
e=a+d # bool convert to 1 or 0
print(e)


# Explicit str to int float
s='135'
i=10+int(s) # str to int conversion
f=float(s) # str to float conversion
print(i)
print(f)


# List, tuple str conversion 1
s='geeks'
print('str to list', list(s))
print('str to tuple', tuple(s))
print('', set(s))


# to str
l=['a','b','c']
print('list to str', str(l))

a=10
b=11
print('int to str,', str(a)+str(b))

c=12.5
print('float to str', str(c))


# to list
t=(10,20,30)
print('tuple to list', list(t))

s={10,20,30}
print('set to list', list(s))


# Int to binary
a=20
print('int to binary 20-->', bin(a))
print('int to hexa 20-->', hex(a))
print('int to octa 20-->', oct(a))


# Binary to int
a="1001"
print('binary to int', int(a,2)) # base is 2

b="12"
print('oct to int', int(b,8)) # base is 8

c="A1"
print('hexa to int', int(c,16)) # base is 16




