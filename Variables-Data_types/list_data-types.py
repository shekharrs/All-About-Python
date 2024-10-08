# list data types🔥

# Example Program for list insert and search functions.
l = [10,20,30,40,50]

l.append(30)
print(l)

l.insert(1,15)
print(l)
print(15 in l)
print(l.count(30))
print(l.index(30))
print(l.index(30,4,7))

# Example Program to demonstrate removal of items
l=[10,20,30,40,50,60,70,80]

l.remove(20)
print(l)
print(l.pop())
print(l)
print(l.pop(2))
print(l)

del l[1]
print(l)

del l[0:2]
print(l)


# Some general purpose 
# functions

l=[10,40,20,50]
print(max(l))
print(min(l))
print(sum(l))

l.reverse()
print(l)

l.sort()
print(l)