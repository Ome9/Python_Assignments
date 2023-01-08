z=input()
lst=[]
b=z.split("[")
i=0
if len(b)>2:
    c=z.split(",")
    print(len(c))
else:
    print("cannot unpack")
    
    