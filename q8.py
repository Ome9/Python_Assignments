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
    