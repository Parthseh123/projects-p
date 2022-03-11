username = input("Enter Your username : ")

if(len(username) > 10):
    print("The username contains more than 10 characters")
elif(len(username) == 10):
    print("The username contains 10 characters")
else:
    print("The username contains less than 10 characters")