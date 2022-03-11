ymarks= int(input("Enter your marks of english out of 100 - "))

if(ymarks <= 10 and ymarks > 0):
    print("You are failed in english")
elif(ymarks > 10 and ymarks <= 25):
    print("You got E grade in english")
elif(ymarks > 25 and ymarks <= 45):
    print("You got D grade in english")
elif(ymarks > 45 and ymarks <= 65):
    print("You got C grade in english")
elif(ymarks > 65 and ymarks <= 85):
    print("You got B grade in english")
elif(ymarks > 85 and ymarks <= 100):
    print("You got A grade in english")
else:
    print("Enter valid marks")
