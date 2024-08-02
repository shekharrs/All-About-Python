import sys

print("""Please Select Operation:
1. Add
2. Substract
3. Multiply""")
choice = int(input("Select operation from 1,2,or 3: "))
if choice not in (1,2,3) :
    print("Invalid choice")
    sys.exit()

a = int(input("Enter a first number: "))
b = int(input("Enter the second number: "))

if choice == 1 :
    res = a+b
elif choice == 2 :
    res = a-b
else :
    res = a*b
print("Result is", res)            