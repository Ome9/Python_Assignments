n=input()
inv=True
m=n.split(",")
a=("q","w",'e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m')
b=('Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M')
c=('1','2','3','4','5','6','7','8','9','10')
d=("$","#","@")
for i in range(0,len(m)):
    q=0
    w=0
    r=0
    t=0
    if 5<len(m[i])<13:
        l=[]
        for j in m[i]:
            l.append(j)
        for k in range(len(l)):
            if l[k] in a:
                q=q+1    
            elif l[k] in b:
                w=w+1
            elif l[k] in c:
                r=r+1
            elif l[k] in d:
                t=t+1
        if q==0 or w==0 or r==0 or t==0:
            break
        else:
            print(m[i])
            inv=False
if inv==True:
    print("invalid")	 	  	 	  		    	  		    	      	 	
