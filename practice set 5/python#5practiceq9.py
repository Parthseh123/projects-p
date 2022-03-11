a = {1,2,["aata","bread"]}# sets cannot contain lists

a[["aata","bread"]] = ["aata","bread",1,2]# it is unhashable
print(a)