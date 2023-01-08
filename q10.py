'''
There is a crime scene (let’s say burglary) happened and the forensic people collected a 
hair sample from that scene. Now it is the task of the forensic person to checkout DNA sequence 
of the hair sample is matching with the suspected person (say X) or not.

[Hint: The DNA sequences are unique for every individual. That is, one person’s DNA sequence should
not repeat for another person’s DNA. Thus, the uniqueness is identified through the maximum count of
repetition of code “AGCT” subsequence (as shown below).

###For Diagram refer to the Diagram file in the repo.####

Write a python code that accepts the hair sample DNA sequence as well as Person X DNA sequence. 
If there is exact match of position and maximum count of AGCT sequence, there is a match; otherwise, 
it is a mismatch. Also, if the input sequence has anything apart from AGCT and their combinations, 
it is a clear mismatch irrespective of count and position.
Input Format:
DNA sequence code of hair sample
DNA sequence code of person X
Output Format:
MATCH/MISMATCH
'''

import re
a= input()
b=input()
c=[]
d=[]
for k in a:
    if re.search('[AGCT]',k):
        f=True
    else:
        f=False
for z in b:
        if re.search('[AGCT]',b):
            f1=True
        else:
            f1=False
if f and f1:
        x=re.finditer ("AGCT", a)
        for n in x:
            n1=n.span()
            c.append(n1) 
        y=re.finditer ("AGCT", b)
        for m in y:
            m1=m.span()
            d.append(m1)
        if c==d:
            print("MATCH")
        else:
            print("MISMATCH")
else:
    print("MISMATCH")