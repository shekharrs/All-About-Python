# String in Python🔥

# String🤘

"""
# Ord and chr
print(ord("a"))     # chr to ord
print(ord("A"))
print(chr(97))      # ord to chr
print(chr(65))

# Indexing
s = "geek"
print(s)
print(s[0])
print(s[-1])
print(s[1])
print(s[-2])

# Strings are immutable
s = "geek"
s[0] = "e"  # error: item assignment not supported
print(s)

# Multiline string
s = """
# statement
"""
print(s)

"""

######################################################################

# Escape Sequences and Row Strings🤘

courseDetails = "Hello, Welcome to Geek\'s course"  # backslash[\] to use escape in string
print(courseDetails)

coreSubject = "Hey, \nyou are enrolled in DSA program"  #backslash n [\n] to enter in a new line
print(coreSubject)

# Escaping the backslash itself
s1="A simple \ example"
print(s1)
s2="Backslash at the end\\"
print(s2)
s3="\\n"
print(s3)
s4="\\t"
print(s4)

# Raw string
s1="c:\project\name.py"
print(s1)

s2=r"c:\project\name.py"
print(s2)