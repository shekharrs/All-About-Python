# Find the Leap Year 

y = int(input("Enter a number: "))

if y % 4 == 0 and y % 100 != 0 :
    print("YES")
elif y % 400 == 0 :
    print("YES") 
else :
    print("NO")       