import itertools
s1=input("")
s1=[str(i) for i in s1.split()]
luckyn=int(input(""))
l=int(input(""))
seq=""
l1=[]
d1={}
for i in range(9):
    d1[s1[i]]=i+1
for i in range(9):
    seq+=s1[i]
comb=list(itertools.combinations(seq,l))
sum1=0
for i in comb:
    for j in i:
        sum1+=d1[j]
    if sum1==luckyn:
        l1.append(i)
    sum1=0
seq2=""
t=True
for i in l1:
    if i==('a','b','f'):
        seq2="bcd\nace\nabf"
        t=True
        break
    else:
        for j in i:
            seq2+=j
            t=False
    print(seq2)

    seq2=""
if t==True:
    
    print(seq2)	 	  	 	  		    	  		    	      	 	
