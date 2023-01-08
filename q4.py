'''
A team has maximum 7 members. They have to fill a form indicating their name and age in the format of name:age. The data collector task is converting all the team members given data to list and give it as input to network admin. The Network admin will perform modifications in the given list based on the following conditions. (Dictionary) 

If anyone shares same age, their names are merged together as single name and their ages should be cube rooted.
If anyone shares same name, their ages should be merged together, and the duplicate names are to be removed.
If any of the input is in wrong format (say age:name instead of name:age), that should be verified and modified in the correct format (name: age)

Sample Input= [{"ajay":27},{"Sanjay":28},{"Prathap":15}, {"Vikrant":27}]

Sample Output= [{"ajayVikrant":3}, {"Sanjay":28},{"Prathap":15}]
'''

#CODE#

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
                	 	  	 	  		    	  		    	      	 	
