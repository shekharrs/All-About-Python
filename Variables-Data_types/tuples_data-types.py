# Tuples🔥 - tuples are immutable

# Creating tuple
t=(10,20,"geek")
print(t)

t=()
print(type(t))
print(t)

t=10
print('expected type tuple, but its int',type(t))

t=(10,)
print('created single item tuple',type(t))


# Accessing
t=10,20,30,40,10
print(t[2])
print(t[-1])
print(t[1:3])
print(len(t))
print(t.count(10))
print(t.index(10))