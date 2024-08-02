# Logical Operator 🤖

# AND , OR , NOT🔥
a = 10
b = 20
c = 30

print('AND - both should be true: a < b and b < c', a < b and b < c)        # AND
print('OR - atleast one should be true: a < b or b < c', a < b or b < c)    # OR
print('NOT - if it is true then it will turn to false: a < b', not a < b)   # NOT



# Container and bool🔥
s1 = ''
s2 = s1 or "DefaultStr"
print('In case of false, default value taken s2: ',s2)

l1 = []
l2 = l1 or [1,2,3]
print('In case of true , default value taken l2: ',l2)



# Int value and bool🔥
x = 10

print(" x or 30: ", x or 30)  # in "or" if 1st value is true, 2nd not considered

y = 0

print("y or 30", y or 30)  # 

z = 40

print(" z and 50:", z and 50)  # in "and" value till last is considered,
