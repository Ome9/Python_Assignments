'''
There is a hostel room allocation policy followed in the institution based on marks. Initially, a student
 can choose any room from room numbers 1 to 1000. If the overall mark in a semester is less than 50%, he 
 will be allotted last palindrome number in the range [100 and 200 + percentage value]. In case, the 
 overall mark in a semester is more than 50%, he will be allotted a room between 
 [300 + percentage value and 450] such that it should be last Ramanujan number in that range. 
 If there is no Ramanujan number available in that range, he can avail a room number of last perfect 
 square number in that range. Write a python function to implement the above scenario.
'''

#CODE

num=int(input())
x=0
if num<50:
    for i in range(100,200+num):
        if str(i)==str(i)[::-1]:
            x=i
    print(x)
if num > 50:
    for i in range(300 + num, 450):
            for j in range(1, i):
                for k in range(1, i):
                    if j ** 3 + k ** 3 == i:
                        x = i
    if x == 0:  
        for i in range(300 + num, 450):
         if int(i ** 0.5) ** 2 == i:
             x = i
    print(x)