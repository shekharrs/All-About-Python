# Count Digits in Python

n = int(input("Enter a number: "))

res = 0 
while n > 0 :
    n = n // 10
    res = res + 1
print("Count of digits is", + res)