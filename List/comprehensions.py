# Comprehensions in Python
"""
# l1 = []
# for x in range(11):
#     if x % 2 == 0:
#         l1.append(x) 
# print("Even- ",l1)

l1 = [x for x in range(11) if x % 2 == 0]  # Short method 
print(l1)

# l2 = []
# for x in range(11):
#     if x % 2 != 0:
#         l2.append(x)
# print("Odd- ",l2)


l2 = [x for x in range(11) if x % 2 != 0]  # Short method
print(l2)

"""
#####################################################################

# Functions to get a list that contains all those items of l that are smaller than x.

"""
def getSmaller(l,x):
    return[e for e in l if e < x]

l = [13,15,19,5,2,4,9,10]
x = 10

print(getSmaller(l,x))

"""

#####################################################################

# Returns two lists. The first list contains all even elements of l and second contains odd.
"""
def getEvenOdd(l):
    even = [x for x in l if x % 2 == 0]
    odd = [x for x in l if x % 2 != 0]
    return even, odd

l = [0,1,2,3,4,5,6,7,8,9,10]
even, odd = getEvenOdd(l)
print("Even: ",even)
print("Odd: ",odd)

"""
#####################################################################

# List Comprehensions

"""
s = "geeksforgeeks"
l1 = [x for x in s if x in "aeiou"]
print(l1)

l2 = ["geeks", "ide", "courses", "gfg"]
l3 = [x for x in l2 if x.startswith("g")]
print(l3)

l4 = [x*2 for x in range(6)]
print(l4)

l5 = ["geeks", "ide", "courses", "gfg"]
l6 = [x.upper() for x in l5 if x.startswith("g")]
print(l6)

"""
#####################################################################

# Set,dict comprehension
"""
l = {10,20,3,4,10,20,7,3}

s1 = {x for x in l if x%2==0 }
s2 = {x for x in l if x%2!=0 }  # set comprehension

print(s1)
print(s2)

"""

#####################################################################
l1 = [1,3,4,2,5]

d1 = {x:x**3 for x in l1}
print(d1)

d2 = {x:f"ID{x}" for x in range(5)} # dictionary comprehension
print(d2)


l2 = [101,103,102]
l3 = ['gfg','ide','corse']

d3 = {l2[i]:l3[i] for i in range(len(l2)) }   # dictionary comprehension
print(d3)

d4 = dict(zip(l2,l3))   # inbuilt zip method
print(d4)

#####################################################################

# Inverting dict

d1 = {101:'gfg', 103:'practice', 102:'ide'}
d2 = {v:k for (k,v) in d1.items()}
print(d2)
