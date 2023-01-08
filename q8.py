'''
Let’s assume you posted a story in social media which goes viral today. However, haters try to troll the 
content and attacking your comment section! As to neutralize the threat in the comment section, one way of 
dealing this situation is to remove all of the vowels from the trolls’ comments. 
Design a python code that takes a string argument and returns a new string with all vowels removed.
'''

#CODE
s=input()
az={"a","e","i","o","u","A","E","I","O","U"}
s1=[]
for i in range(len(s)):
    if s[i] not in az:
        s1.append(s[i])
    else:
        pass
    if s=="aeiou":
        print("NIL")
        break
print("".join(s1))        
    