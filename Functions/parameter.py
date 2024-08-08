# Parameter Passing in Python

# Assigning and modifying
# def fun(x):
#     x = 15

# x = 10
# fun(x)
# print(x)


# def fun(l):
#     l.append(15)

# l = [10,20,30]
# fun(l)
# print(l)


# Id of parameter
def fun(x):
    print(id(x))
    x = 15
    print(id(x))
x = 10
fun(x)
print(id(x))


def fun(l):
    print(id(l))
    l.append(15)
    print(id(l))
l = [10,20,30]
fun(l)
print(id(l))    


