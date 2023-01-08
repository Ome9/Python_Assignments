z=input()
a=len(z)
count=0
if z.isalpha():
    if a%2!=0:
        z1=int((a-1)/2)
        for i in range(z1+1):
            if z[z1-i]==z[z1+i]:
                count+=1
            else:
                break
        if count>1:
            print((2*count)-1)
        else:
            print("1")
    elif a%2==0:
        q1=int(a/2)
        for j in range(q1):
            if z[(q1-1)-j]==z[q1+j]:
                count+=1
            else:
                break
        if count>1:
            print(2*count)
        else:
            print("1")
else:
    print("invalid input")	 	  	 	  		    	  		    	      	 	
