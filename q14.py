'''
There are “n” customers who buy ‘m” products in an online mart. Write a python code which accepts 
customerId, Product, Quantity, rate from console. The program should execute the following transactions
using functions: 

1. Fn1(): Given a customerID, display the total amount paid by the customer 
2. Fn2() : Find and display the product which has maximum and minimum orders placed. 
3. Fn3(): Find the customer who has maximum order placed. Prepare a final bill according to the 
          given format as given below and write it to a file.

Input Format

No. of Customers: n 
No. of products: m
customerID
Product
Quantity
Rate

Output Format

customerId,Product,Quantity,rate,TotalPrice
111,Soap,1,45.00,45.00
222,Book,2,100.00,200.00
333,Pen,1,20.00,20.00
444,Inkbottle,1,50.00,50.00

TotalAmount: Rs:315
'''
#CODE

l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
tot=0
n=int(input())
m=int(input())
for i in range ((n)):
    cid=input()
    l1.append(cid)
    p=input()
    l5.append(p)
    q=int(input())
    l3.append(q)
    r=float(input())
    l4.append(r)
    for i in range(q+1):
        l2.append(p)
def fn1(a):
    b=l3[l1.index(a)]*l4[l1.index(a)]
    return b
def fn2():
    f={}
    for i in l2:
        if i in f:
            f[i]+=1
        else:
            f[i]=1 
    a=list(f.keys())[list(f.values()).index(max(list(f.values())))]
    b=list(f.keys())[list(f.values()).index(min(list(f.values())))]
    return a,b
def fn3():
    return (l1[l3.index(max(l3))])
a=input()
out1=fn1(a)
out2=fn2()
out3=fn3()
print(out1)
for i in out2:
    print(i)
print(out3)
for i in range(n):
    bill=f"{l1[i]},{l5[i]},{l3[i]},{l4[i]},{l3[i]*l4[i]}"
    print(bill)
    tot+=l3[i]*l4[i]
print(f"TotalAmount: Rs:{int(tot)}")