Username = "Parth"
diarynickname = "DiBuddy"

passwordfw = open("password")
pinsidef= passwordfw.read()
if("defualt" == pinsidef or "" == pinsidef):
    password = input("Enter password you want to set - ")
    passwordfw = open("password","w")
    passwordfw.write(password)
# with open(password.txt, 'r') as f:
#     a = f.read()
passwordfw = open("password")
pinside= passwordfw.read()
n=0

diary_code = {}

def addorsee():
    duwtwd=input("Do you want to wish diary - ")
    if("yes"==duwtwd):
                print("You: Hi buddy")
                print("Diary: Hello",Username,"I hope u r fine buddy")
    add_or_see = input("Do you want to add or see - ")
    while(n < 10):
        if("add" in add_or_see):

            addtitle = input("Enter you title - ")
            add1page=input("Enter your text - ")
            diary_code.update({addtitle : add1page})
            pagefile = open(addtitle,"w")
            pagefile.write()
            
            add_or_see = input("Do you want to add or see - ")

        if("see" in add_or_see):
            pgnumber=input("Enter the page number you want to see - ")
            print(diary_code[addtitle])
            add_or_see = input("Do you want to add or see - ")


                

open = input("Enter The password to open the diary - ")
if(open == pinside):
    addorsee()    
else:
    print("try again")
    open = input("Enter The password to open the diary - ")
    if(open in pinside):
        addorsee()    
    else:
        print("try again")
        open = input("Enter The password to open the diary - ")
        if(open in pinside):
            addorsee()
        else:
            print("Diary Locked")






