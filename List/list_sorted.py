# Check if a list is sorted🔥

# def isSorted(l):
#     i = 1
#     while i < len(l):
#         if l[i] < l[i-1]: 
#             return False
#         i = i + 1
#     return True

# l = [10,20,30,40]
# if isSorted(l):
#     print("YES")
# else:
#     print("NO")    

#####################################################################

# Using sorted() method

def isSorted(l):
    l2 = sorted(l)

    if l == l2:
        return True
    else :
        return False

l = [10,20,30,15,40]
if isSorted(l):
    print("YES")
else:
    print("NO")      