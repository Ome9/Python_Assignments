'''
Calculate the following numbers in numerology using below table. (using Set only)
###For Diagram Refer to the Diagrams file.###
a. Destiny number (sum of the numerical value assigned to each letter in the name up to single digit) Ex: TEENA (2+5+5+5+1=18=1+8=9) 
b. Soul urge number/Heart’s desire number (sum of the numerical value assigned to each VOWEL in the name up to single digit) Ex: TEENA (5+5+1=11=2) 
c. Dream number (sum of the numerical value assigned to each CONSONANT in the name up to single digit) 

Ex: TEENA (2+5=7)

Inputs:
Enter name

Output:
Destiny number
Soul urge number
Dream number

Input=TEENA 

Output=9
2
7
'''


z=input()
l=[]
num=0
num1=0
num2=0
S1={"A","J","S"}
S2={"B","K","T"}
S3={"C","L","U"}
S4={"D","M","V"}
S5={"E","N","W"}
S6={"F","O","X"}
S7={"G","P","Y"}
S8={"H","Q","Z"}
S9={"I","R"}
for i in range(0,len(z)):
    l.append(z[i])
#Destiny number    
for i in l:
    if i in S1:num+=1
    if i in S2:num+=2    
    if i in S3:num+=3
    if i in S4:num+=4
    if i in S5:num+=5
    if i in S6:num+=6
    if i in S7:num+=7
    if i in S8:num+=8
    if i in S9:num+=9
v={"A","E","I","O","U"}
#Soul urge number
for j in l:
    if j in v:
        if j in S1:num1+=1
        if j in S2:num1+=2    
        if j in S3:num1+=3
        if j in S4:num1+=4
        if j in S5:num1+=5
        if j in S6:num1+=6
        if j in S7:num1+=7
        if j in S8:num1+=8
        if j in S9:num1+=9     
    else:
        if j in S1:num2+=1   #Dream number
        if j in S2:num2+=2    
        if j in S3:num2+=3
        if j in S4:num2+=4
        if j in S5:num2+=5
        if j in S6:num2+=6
        if j in S7:num2+=7
        if j in S8:num2+=8
        if j in S9:num2+=9
temp=0
temp1=0
temp2=0
if len(str(num))>1:
    for u in str(num):
        temp+=int(u)
    print(temp)    
else:
    print(num)
       
if len(str(num1))>1:
    for o in str(num1):                
        temp1+=int(o)
    print(temp1)    
else:
    print(num1)
if len(str(num2))>1:
    for p in str(num2):
        temp2+=int(p)
    print(temp2)    
else:
    print(num2)	 	  	 	  		    	  		    	      	 	
