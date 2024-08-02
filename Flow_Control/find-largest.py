# Find the Largest number in python

# find the largest number from a, b , c

# a = int(input("Enter a First Number: "))
# b = int(input("Enter a Second Number: "))
# c = int(input("Enter a Third Number: "))

# if (a >= b) and (a >= c) :
#     print("a is the largest number")
# elif (b >= a) and (b >= c) :
#     print("b is the largest number")    
# elif (c >= a) and (c >= b) : 
#     print("c is the largest number")



# finding the largest number among a,b,c
# a = int(input("Enter a first number: "))
# b = int(input("Enter a second number: "))
# c = int(input("Enter a third number: "))

# if a >= b :
#     if a >= c :
#         print(a, "is the largest number")
#     else : 
#         print(c, "is the largest number")

# else : 
#     if b >= c :
#         print(b, "is the largest number")
#     else :
#         print(c, "is the largest number")            



a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))

print(max(a,b,c))