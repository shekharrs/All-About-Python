# String Operations in Python🔥

# Checking for substring🤘
s1 = "geeksforgeeks"
s2 = "geeks"

print(s2 in s1)
print(s2 not in s1)

# Concatenation🤘
s1 = "geeks"
s2 = "for"
s3 = s1 + s2
s4 = "welcome to " + s1 + s2
print(s3)
print(s4)

# Position of substring🤘
s1 = "geeksforgeeks"
s2 = "geeks"
print(s1.index(s2))
print(s1.rindex(s2))        # right index
print(s1.index(s2,1,13))    # start and end index

# Len,lower,upper🤘
s1 = "geeks"

print(len(s1))

s2 = s1.upper()

print(s2)

s3 = s2.lower()

print(s3)

print(s1.islower())

print(s2.isupper())

# Startwith ,endwith🤘
s = "GeeksforGeeks Python Course"

print(s.startswith("Geeks"))

print(s.endswith("Course"))

print(s.startswith("Geeks", 1))     # start index

print(s.startswith("Geeks",8,len(s)))   # start index, last-index

# Split join🤘
s1 = "geeks for geeks"

print(s1.split())   # split by space ' '

s2 = "geeks, for, geeks"
print(s2.split(','))        # split by comma ','

l = ["geeksforgeeks","python","course"]

print(" ".join(l))          # join by space

print(", ".join(l))         # join by comma

# Strip🤘
s1 = "__geeksforgeeks__"

print(s1.strip("_"))   # strip from both side


print(s1.lstrip('_'))  # strip from left side


print(s1.rstrip("_"))   # strip from right side

# Find🤘
s1 = "geeks for geeks"

s2 = "geeks"

print(s1.find(s2))

print(s1.find("gfg"))

n = len(s1)

print(s1.find(s2,1,n))