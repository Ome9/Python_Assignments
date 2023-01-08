'''
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users (using tuples only) 
Following are the criteria for checking the password: 

1. At least 1 letter between [a-z] 

2. At least 1 number between [0-9] 

3. At least 1 letter between [A-Z] 

4. At least 1 character from [$#@] 

5. Minimum length of transaction password: 6 

6. Maximum length of transaction password: 12 

Your program should accept a sequence of comma separated passwords and will check 
them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a 
comma. If none of the password is valid, you should print “invalid”

Sample Input= ABd1234@1,a F1#,2w3E*,2We3345 

 Sample Output= ABd1234@1
'''
#CODE#
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
