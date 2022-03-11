print("Scrambled words")
print("Try to guess the right one")
p=0

for i in range(100):
    a=input("atbiliy - ")
    if("ability" in a):
        p+=1
        print("You guessed it right")
        print("Score:",p)
        for i in range(100):
            b=input("blea - ")
            if("able" in b):
                p+=1
                print("You guessed it right again")
                print("Score:",p)
                for i in range(3):
                    c=input("otaub - ")
                    if("about" in c):
                        p+=1
                        print("You guessed it right")
                        print("Score:",p)
                        for i in range(3):
                            d=input("ccnairgod - ")
                            if("according" in d):
                                p+=1
                                print("You guessed it right")
                                print("Score:",p) 
                                for i in range(3):
                                    e=input("ecsbeau - ")
                                    if("because" in e):
                                        p+=1
                                        print("You guessed it right")
                                        print("Score:",p)
                                        
                                    else:
                                        print("You guessed it wrong")
                            else:
                                print("You guessed it wrong")
                    else:
                        print("You guessed it wrong")
            else:
                print("You guessed it wrong")
    else:
        print("You guessed it wrong")
print("You lost Start again.")
for i in range(3):
    a=input("atbiliy - ")
    if("ability" in a):
        p+=1
        print("You guessed it right")
        print("Score:",p)


