from os import replace


yname=input("Enter your name - ")
tdate=input("Enter today's date - ")
letter='''Dear <|name|>,
you are selected!
<|date|>
'''
letter=letter.replace("<|name|>",yname)
letter=letter.replace("<|date|>",tdate)