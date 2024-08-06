# Check for Prime Number in Python

# n = int(input("Enter a number: "))

# if n <= 1 :
#     print("No")
# else :
#     for i in range(2, n) :
#         if n % i == 0 :
#             print("No")
#             break
#     else :
#         print("Yes")
    
##################################################

# Using  Optimize Solution

n = int(input("Enter a number: "))

if n <= 1 :
    print("No")
else :
    x = 2
    while x*x <= n :
        if n % x == 0 :
            print("No")
            break
        x = x+1

    else :
        print("Yes")    