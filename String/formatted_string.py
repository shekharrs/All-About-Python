# Formatted String in Python🔥

# 3 formatted string are there in pythons👇

# Percent (%) Formatting: This is the oldest method, using the % operator to format strings.
# str.format() Method: Introduced in Python 3, this method uses curly braces {} as placeholders.
# F-Strings (Formatted String Literals): Available from Python 3.6, f-strings are prefixed with f and allow embedding expressions inside string literals.

# Percent (%) Formatting
name = "ABC"
course = "Python Course"

s = "Welcome %s to the %s"%(name,course)
print(s)
print()

# str.format() Method
s = "welcome {0} to the {1}".format(name,course)
print(s)
print()

# F-Strings (Formatted String Literals)
s = f"welcome {name} to the {course}"
print(s)
print()