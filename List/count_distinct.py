# Count distinct Element in Python🔥

# def disElement(l):
#     res = 1

#     for i in range(1,len(l)):
#         if l[i] not in l[0:i]:
#             res = res + 1

#     return res

# l = [10,20,10,30,30,20]
# print(disElement(l))

#####################################################################

# Shortest method

def disElement(l):
    return len(set(l))

l = [10,20,10,30,30,20]
print(disElement(l))

def disElement(l):
    return len(set(l))

l = [10,20,10,30,30,20]
print(disElement(l))