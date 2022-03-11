emarks = int(input("Enter your marks in english out of 40 : "))
hmarks = int(input("Enter your marks in hindi out of 40 : "))
mmarks = int(input("Enter your marks in maths out of 40 : "))

if(emarks<33 or emarks>0 or hmarks<33 or hmarks>0 or mmarks<33 or mmarks>0):
    print("You are failed because of less marks")
elif(emarks>33 or emarks == 40 or hmarks>33 or hmarks == 40 or mmarks>33 or mmarks == 40):
    print("Congratulations! You are passed")
elif(emarks<0 or emarks>40 or mmarks<0 or mmarks>40 or hmarks<0 or hmarks>40):
    print("Enter valid marks")