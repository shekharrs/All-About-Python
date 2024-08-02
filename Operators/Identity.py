# Identity Operator

# 'is' operator - Evaluates to True if the variables on either side of the operator point to the same object and false otherwise.

x = 10
y = 10

print(x is y)
print(id(x))
print(id(y))



# 'is not' operator - Evaluates to false if the variables on either side of the operator point to a different object and true otherwise.

x = 10

y = x

print("x and y has same address:", x is y)  # is operator

print(x is not y)    # is not operator