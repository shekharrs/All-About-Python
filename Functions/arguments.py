# Types of Arguments.🔥
# Python supports various types of arguments that can be passed at the time of the function call.

# Default Arguments👍

# def myFun(x, y = 50):
#     print("x: ", x)
#     print("y: ", y)
# myFun(10)

######################################################

# Keyword Arguments👍

# def printItem(id, name="NA", price="NA"):
#     print(f"Id is {id}")
#     print(f'Name is {name}')
#     print(f'Price is {price}')

# printItem(101, "abc", 100)   # passing parameter by positional-arg
# print()
# printItem(id=102, name="xyz", price=200)  # passing parameter by keyword-arg
# print()
# printItem(name="iky", price=500, id=103)  # passing parameter by keyword-arg, not in order  

######################################################

# Variable Length Arguments👍

# def sum(*elements):      # Non-keyword Arguments
#     res = 0
#     for x in elements:
#         res = res + x
#     return res

# print(sum(10,20))
# print(sum(10,20,30))
# print(sum(10))
# print(sum())    

def printDetails(**details):   # Keyword Arguments
    for d, v in details.items():
        print(f"{d} {v}")

printDetails(id=110, name="abcd", price=304)
print()
printDetails(id=130, name="xyz")
