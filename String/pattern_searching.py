# Pattern Searching in Python

txt = input("Enter Text: ")
pat = input("Enter Pattern: ")

pos = txt.find(pat)
while pos >= 0:
    print(pos)
    pos = txt.find(pat, pos+1)