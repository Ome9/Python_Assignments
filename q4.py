a=eval(input())
b=tuple(a) 
for i in b:
    for j in i:
        if type(j)==int:
            c={i[j]:j}
            a.append(c)
            a.remove(i)
for n in range(1, len(a)):
    k=0
    for l in a[k]:
        if l in a[n]:
            a[k][l]=(str(a[k][l])+ str(a[n][l])) 
            a.remove(a[n])
        else:
            k+=1
for g in range(1, len(a)):
    h=0
    for p in a[h]:
        for s in a[g]:
            if a[h][p]==a[g][s]:
                e={str(p)+str(s):int(a[h][p]**(1/3))}
                a.insert(1,e)
            else:
                h+=1
x=[] 
q=[]
for z in a:
    for v in z:
        x.append(v) 
        q.append(z[v])
for h in a:
    for k in h:
        if x.count(k)>1: 
            a.remove(h)
        if q.count(h[k])>1:
            a.remove(h)
print(a)                
                	 	  	 	  		    	  		    	      	 	
