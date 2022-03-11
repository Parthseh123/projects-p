print("Contact Book")
n=0
while n<10:
    add_or_see = input("Do you want to add or see - ")

    if("add" in add_or_see):

        name = input("Enter Contact name - ")
        connumber=input("Add Number - ")
        pagefile = open(name,"w")
        pagefile.write(connumber)
            
        add_or_see = input("Do you want to add or see - ")

    if("see" in add_or_see):
        nameo=input("Enter the contact name you want to see - ")
        pagefile = open(nameo)
        contactfiler=str(pagefile.read())
        print(nameo,":",contactfiler)
        add_or_see = input("Do you want to add or see - ")