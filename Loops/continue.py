# Continue in Python

# l = [10,16,17,18,19,15]

# for x in l :
#     if x % 5 == 0 :
#         continue
#     print(x)




# Using without continue statement

# l = [10,16,17,18,19,15]

# for x in l :
#     if x % 5 != 0 :
#         print(x)

###########################################

# i = 0
# while i <= 5 :
#     if i == 3 :
#         i = i + 1
#         continue
#     print(i, i*i)
#     i = i + 1

###########################################

# Using continue & break statement

l = [10,16,17,18,9,15,21,13]

for x in l :
    if x % 5 == 0 :
        continue
    if x % 7 == 0 :
        break
    print(x)
print("Bye")    


