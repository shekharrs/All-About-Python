# All Divisors of Number in Python

# Using for loop

# n = int(input("Enter a number: "))

# for x in range(1, n+1) :
#     if n % x == 0 :
#         print(x)

################################################## 

# Using while loop

# n = int(input("Enter a number: "))

# x = 1
# while x <= n :
#     if n % x == 0 :
#         print(x)
#     x = x + 1      

##################################################

# Optimize Solution

n = int(input("Enter a number: "))

x = 1
while x*x < n :

    if n % x == 0 :
        print(x)
        print(n//x)

    x = x+1

    if x*x == n :
        print(x)