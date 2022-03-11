n1 = int(input("Enter your 1st number : "))
n2 = int(input("Enter your 2nd number : "))
n3 = int(input("Enter your 3rd number : "))
n4 = int(input("Enter your 4th number : "))

if(n1>n2):
    b1 = n1
else:
    b1 = n4

if(n2>n3):
    b2 = n2
else:
    b2 = n3
if(n1>n2):
    print(n1,"is greatest")
else:
    print(n2,"is greatest")