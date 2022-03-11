print("Calculator")
a=int(input("Enter first number - "))
b=int(input("Enter second number - "))
mdas=input("Do you want to add subtract multiply or divide - ")

if("a" == mdas):
    print("Sum is",a+b)
if("s" == mdas):
    print("Difference is",a-b)
if("d" == mdas):
    print("quotiant is",a%b)
if("m" == mdas):
    print("product is",a*b)
