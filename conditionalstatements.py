#Q2- Conditional Statements

#Python Code-
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if(a >= b and a >= c):
    print("First number is largest", a)
elif(b >= c):
    print("Second number is largest", b)
else:
    print("Third is largest", c)


#Output
# Enter first number: 10
# Enter second number: 15
# Enter third number: 20
# Third is largest 20




