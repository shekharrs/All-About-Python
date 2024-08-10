# Binary to Decimal in Python🔥

# def binToDec(b):
#     res = 0

#     p = 1
#     for x in reversed(b):
#         res = res + int(x) * p
#         p = p * 2

#     return res

#####################################################

# Direct Method (inbuilt)

def binToDec(b):
    res = int(b,2)
    return res
print(binToDec('1111'))