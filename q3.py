'''
Write a Python code for the following: 

A list has the objects of maximum 2 strings, 2 complex numbers and 2 integers. 
If atleast one integer object is prime, all strings should be reversed and the real part as well as the imaginary part of all the complex numbers should be interchanged.
if atleast one string object is palindrome, all the complex numbers should be conjugated, and the integer objects should be negated. 
If both of the above conditions are satisfied, print the middle element of the list. 
If none of the above conditions satisfied, convert all the strings into list object.

Sample Input
[(5+3j),"Madam",6,-1]
Sample Output
[(5-3j),"Madam",-6,1]
'''
#CODE#

import re
z=input()
s=z[1:(len(z)-1)]
a=s.split(",")
lint=[]
lint1=[]
lstr=[]
lstr1=[]
lcom=[]
lcom1=[]
lcom2=[]
lis=[]
new=[]
condition1=False
condition2=False
for i in a:
    if i.isnumeric():
        lint.append(int(i))
    elif re.search("^-.+",i) and "j" not in i:
        lint.append(int(i))
    elif re.search('[0-9].+j',i):
        i=i.replace(" ", "")
        i1=complex(i)
        lcom.append(i1)
    elif re.search('[A-Za-z].+',i):
        lstr.append(i[1:len(i)-1])     
if len(lint)==0 or len(lcom)==0 or len(lstr)==0:
    print("Invalid Data")
else:
    for j in lint:
        for k in (2, int(abs(j)/2)+1):
            if (j % k) == 0 or j==1 or j==-1:
                break
        else:
            condition1=True
            for q in lstr:
                lstr1.append(q[::-1])
                
            for e in lcom:
                t=int(e.real)
                u=int(e.imag)
                e1=complex(u,t)
                lcom1.append(e1)    
            break        
            
    
    for l in lstr:
        if l.lower()==(l[::-1]).lower():
            condition2=True
            if condition1==True:
                for m in lcom1:
                    q1=m.conjugate()
                    lcom2.append(q1)
                for n in lint:
                    if n>0:
                        q3=-abs(n)
                        lint1.append(q3)
                    elif n<0:
                        q4=abs(n)
                        lint1.append(q4)
                    else:
                        pass
            elif condition1!=True:
                for m in lcom:
                    q1=m.conjugate()
                    lcom2.append(q1)
                for n in lint:
                    if n>0:
                        q3=-abs(n)
                        lint1.append(q3)
                    elif n<0:
                        q4=abs(n)
                        lint1.append(q4)
                    else:
                        pass
    if condition1==True and condition2==False:
        lst3=lstr1+lint+lcom1
        print(lst3)   
    elif condition2==True and condition1==False:
        lst4=lcom2+lstr+lint1
        print(lst4)                 
    elif condition1==True and condition2==True:
        az=len(a)
        print(a[int(((az+1)/2)-1)])    
    elif condition1==False and condition2==False:
        for t in lstr:
            for w in t:
                new.append(w)
            print(new+lint+lcom)
                        

            
        
        
        	 	  	 	  		    	  		    	      	 	
