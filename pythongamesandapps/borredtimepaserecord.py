
print("Try to build a record")
fl=0
while fl < 10:
    sop=input("Do you want to play or see your current record - ")
    h=open("number.txt","w")
    h.write("0")
    if("play" in sop):
        for i in range(1,100000):
            if(100 == i or 1000 == i):
                s=input("Do you want to quit now - ")
                if("quit" in s):
                    h.write(str(a+1))
                    break
            a=int(input("Start counting - "))
            if(a==i):
                print("You have reched",i)
                h=open("number.txt","w")
                h.write(str(a))
            else:
                print("You wrote the wrong one.")
                break
        # print("Congrats on completing this game")
    if("see" in sop):
        l=open("number.txt","r")
        ll=l.read()
        print("Highscore:",ll)
        





