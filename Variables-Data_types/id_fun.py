# id() function👽

print(id(5))

a = 10
print('id of a',id(a))

b = a
print('id of b',id(b))

# same value literals stored at same location
a = 10
b = 10
print(id(a)) 
print(id(b))

c ="geeks"
d ="geeks"

print('id c',id(c))
print('id d',id(d))