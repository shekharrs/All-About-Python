# Nested Loop

# for i in range(1, 1*10+1, 1) :
#     print(i, end=" ")
# print()
# for i in range(2, 2*10+1, 2) :
#     print(i, end=" ")
# print()
# for i in range(3, 3*10+1, 3) :
#     print(i, end=" ")
# print()        

# Using Nested Loop👇

# for i in range(1, 11) :
#     for j in range(i, i*10+1, i) :
#         print(j, end=" ")
#     print()      


###########################################
# while loop

# for i in range(1,3) :
#     j = 1 
#     while j < 3 :
#         print(i,j)
#         j = j + 1
#     print("Hey!!")  

###########################################
# list of list

ll = [[10,20,30],[40,50,60],[70,80]]

for l in ll :
    for x in l :
        print(x, end=" ")
    print()    