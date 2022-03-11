dic = {}
namea = str(input("enter 1st freind name : "))
langa = str(input("enter your favourite language : "))
nameb = str(input("enter 2nd freind name : "))
langb = str(input("enter your favourite language : "))
namec = str(input("enter 3rd freind name : "))
langc = str(input("enter your favourite language : "))
named = str(input("enter 4th freind name : "))
langd = str(input("enter your favourite language : "))

dic.update({namea : langa})
dic.update({nameb : langb})
dic.update({namec : langc})
dic.update({named : langd})

print(dic) #the 1st freind favourate language will be overwritten