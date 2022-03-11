for i in range(100):
    num = int(input("Enter the number - "))
    prime = True
    for i in range(2,num):
        if(num%i == 0):
            prime = False
            break
    
    if prime:
        print("It is prime")
    else:
        print("it is not prime")