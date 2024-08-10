# Decimal to Binary in Python

# def decimalToBinary(n):
#     if n == 0:
#         return "0"
#     res = ""
#     while n > 0:
#         res = res + str(n % 2)
#         n = n // 2
#     return res[::-1]

# for i in range(1, 16):
#     print(i,decimalToBinary(i))

#####################################################

# Direct Method (inbuilt method)

def decToBin(n):
    res = bin(n)
    return res[2:]

for i in range(1,16):
    print(i,decToBin(i))
