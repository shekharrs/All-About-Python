# String Operations in Python🔥

# Checking for substring
s1 = "geeksforgeeks"
s2 = "geeks"

print(s2 in s1)
print(s2 not in s1)

# Concatenation
s1 = "geeks"
s2 = "for"
s3 = s1 + s2
s4 = "welcome to " + s1 + s2
print(s3)
print(s4)

# Position of substring
s1 = "geeksforgeeks"
s2 = "geeks"
print(s1.index(s2))
print(s1.rindex(s2))        # right index
print(s1.index(s2,1,13))    # start and end index
