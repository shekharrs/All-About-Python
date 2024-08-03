# Patterns

# Square Pattern

# n = int(input("Enter a number: "))

# for i in range(n) :
#     for j in range(n) :
#         print("*", end=" ")
#     print()    

# Triangle Pattern

# n = int(input("Enter a number: ")) 

# for i in range(n) :
#     for j in range(i+1) :
#         print("*", end=" ")
#     print()    

# Inverted Triangle Pattern

n = int(input("Enter a number: "))

for i in range(n) :
    for j in range(n-i) :
        print("*", end=" ")
    print()     
