'''
Implement a bus reservation system for the route Bangalore to Chennai using files and functions. 
Read the credentials (user name and password) from the file ("credentials.txt") and match it for 
further processing. If the credentials are not matching, then print "Invalid Credentials" and terminate 
the program.
There are 15 seats available in the bus with following tariff. Reservation will be performed in first 
come first serve basis. Calculate the fare using function. Print the passenger details, departure, arrival 
station, seat no, booking dates and total fare. (Use Booking Date as 15-11-2022). Save the details in 
the file ("reservation.txt")

Main Menu
------------
1. Booking
2. Cancellation
3. Exit

Booking Menu
------------
A. Regular (12 seats) 
B. Tatkal (3 seats)

Fare details from Bangalore
------------
Regular:
Hosur Rs75
Vaniyambadi Rs 250
Vellore Rs 500
Walaja Rs600
Chennai Rs750
*for senior citizen 10% concession (Age 60 and above)
Tatkal Booking fare - Rs100 addition to the regular fare

Cancellation Refund Details
----------------------------
20 days before the date of journey - full refund
2 weeks before the date of journey - 90% fare refund
1 week before the date of journey - 80% fare refund
4 days before the date of journey - 50% fare refund
<4 days - No refund

Input Format
----------------------
Username
Password

Main Menu Choice

If option choosen as 1
------------------------------
Booking Menu Choice
No. of passengers
Passenger-1 details (Name, Age)
Passenger-2 details (Name, Age)
.
.
Passenger-N details (Name, Age)
Travel Destination
Date of Journey

Main Menu Choice

if option choosen as 2
----------------------------------
Passenger Name and Age
Date of Cancellation

Output Format
---------------------------
Remaining Seats:
Regular =
Tatkal =
Journey Details:
Passenger Name - Age - Source - Destination - Seat No
Date of Journey:
Total Fare =

####################

Test case 1
----------------------

input
-----------
abc
123
1
A
3
Arun, 39
sheethal, 34
karthik, 70
Chennai
25-11-2022
1
B
3
Akash, 53
Rhea, 15
Sam, 26
Vellore
17-11-2022
1
B
2
Bhoomi, 25
Saransh, 60
Walaja
16-11-2022
3

output
-------------
Remaining Seats:
Regular = 9
Tatkal = 3
Passessnger Name - Age - Source - Destination - Seat No
Arun - 39 - Bengaluru - Chennai - 15
sheethal - 34 - Bengaluru - Chennai - 14
karthik - 70 - Bengaluru - Chennai, 13
Date of Journey: 25-11-2022
total fare = Rs. 2175
Remaining Seats:
Regular = 9
Tatkal = 0
Passessnger Name - Age - Source - Destination - Seat No
Akash - 53 - Bengaluru - Vellore - 12
Rhea - 15 - Bengaluru - Vellore - 11
Sam - 26 - Bengaluru - Vellore - 10
Date of Journey: 17-11-2022
total fare = Rs. 1800
insuffient seats!!! Try for other dates...

Test case 2
----------------------

input
-----------
abc
123
1
A
3
Arun, 39
sheethal, 34
karthik, 70
Chennai
25-11-2022
1
B
3
Akash, 53
karthik, 15
Sam, 26
Vellore
20-11-2022
2
karthik
15
15-11-2022
3

output
-------------
Remaining Seats:
Regular = 9
Tatkal = 3
Passessnger Name - Age - Source - Destination - Seat No
Arun - 39 - Bengaluru - Chennai - 15
sheethal - 34 - Bengaluru - Chennai - 14
karthik - 70 - Bengaluru - Chennai, 13
Date of Journey: 25-11-2022
total fare = Rs. 2175
Remaining Seats:
Regular = 9
Tatkal = 0
Passessnger Name - Age - Source - Destination - Seat No
Akash - 53 - Bengaluru - Vellore - 12
karthik - 15 - Bengaluru - Vellore - 11
Sam - 26 - Bengaluru - Vellore - 10
Date of Journey: 20-11-2022
total fare = Rs. 1800
Remaining Seats:
Regular = 9
Tatkal = 1
No. of Passessngers to Cancel = 1
Cancelled Passessnger Name = karthik
Cancelled Passessnger Age = 15
Refund Amount = Rs. 300
Cancellation Charge = Rs. 300
'''

#CODE

import datetime
import linecache
#Change the file path according to your file destination
passd=linecache.getlines(r'C:\Users\omkar\OneDrive\Desktop\credentials.txt',0)[1][0:3] 
user=linecache.getlines(r'C:\Users\omkar\OneDrive\Desktop\credentials.txt',0)[0][0:3]
file=open(r"D:\reservation.txt","w+")
user_in=input()
passd_in=input()
TS=15
NOTT=3
NOTB=12
Info1=[]
Info2=[]
Ages=[]
Fair=[]
Ages2=[]
Fair2=[]
Name_Fair=[]
Name_Fair2=[]
Fare_Details={"Hosur":75,"Vaniyambadi":250,"Vellore":500,"Walaja":600,"Chennai":750}
if user==user_in and passd==passd_in:
    while True:
        choice=int(input())
        if choice==1:
            booking_choice=input()
            if booking_choice=="A":
                NOP_R=int(input())
                if NOP_R>NOTB:
                    file.write("insuffient seats!!! Try for other dates...\n")
                    for m in range(NOP_R):
                        flush_detail=input()
                    flush_loc=input()
                    flus_date=input()
                    pass
                if NOP_R<=NOTB:
                    for i in range(NOP_R):
                        P_Detail_R=input()
                        p=P_Detail_R.split(",")
                        name=p[0]
                        age=int(p[1])
                        Ages.append(age)
                        Name_Fair.append(name)
                        Info1.append(f"{name}-{age}-Bengaluru-")
                        NOTB-=1 #counting the no seats left
                    file.write(f"Remaining Seats:\nRegular={NOTB}\nTatkal={NOTT}\n") 
                    file.write("Passessnger Name - Age - Source - Destination - Seat No\n")   
                    Destination=input()
                    for i in Info1:
                        ui=(f"{i}{Destination}-{TS}\n")
                        TS-=1
                        file.write(ui)
                        #writing th final line
                    for j in range(0,len(Name_Fair)):
                        if Ages[j]>=60:
                            Name_Fair.insert((j*2)+1,(int(Fare_Details.get(f"{Destination}"))-int(Fare_Details.get(f"{Destination}"))*0.1))
                            Fair.append((int(Fare_Details.get(f"{Destination}")))-(int(Fare_Details.get(f"{Destination}"))*0.1))   
                        else:
                            Name_Fair.insert((j*2)+1,(int(Fare_Details.get(f"{Destination}"))))
                            Fair.append(int(Fare_Details.get((f"{Destination}"))))
                    for r in range(2,len(Name_Fair)+3,3):
                        Name_Fair.insert(r,"R")        
                    z=input()          #entering the date
                    x=z.split("-")
                    fares=sum(Fair)
                    DOJ=datetime.date(int(x[-1]),int(x[-2]),int(x[-3]))    
                    file.write(f"Date of Journey:{z}\n")
                    file.write(f"total fare=Rs.{int(fares)}\n") 
                    file.write("\n")   
            else:pass    
            if booking_choice=="B":
                NOP_T=int(input())
                if NOP_T>NOTT:
                    file.write("insuffient seats!!! Try for other dates...\n")
                    for m in range(NOP_T):
                        flush_detail=input()
                    flush_loc=input()
                    flus_date=input()
                if NOP_T<=NOTT:
                    for i in range(NOP_T):
                        P_Detail_T=input()
                        z=P_Detail_T.split(",")
                        ag=int(z[1])
                        Ages2.append(ag)
                        nam=z[0]
                        Name_Fair2.append(nam)
                        Info2.append(f"{nam}-{ag}-Bengaluru-")
                        NOTT-=1 #counting the remaining seats
                    file.writelines(f"Remaining Seats:\nRegular={NOTB}\nTatkal={NOTT}\n")
                    file.write("Passessnger Name - Age - Source - Destination - Seat No\n")
                    Destination=input()
                    for k in Info2:
                        ui=(f"{k}{Destination}-{TS}\n")
                        TS-=1
                        file.write(ui)
                        #writing th final line     
                    for l in range(len(Name_Fair2)):
                        if Ages2[l]>=60:
                            Name_Fair2.insert((l*2)+1,((Fare_Details.get(f"{Destination}"))-(Fare_Details.get(f"{Destination}"))*0.1)+100)
                            Fair2.append(((Fare_Details.get(f"{Destination}"))-(Fare_Details.get(f"{Destination}"))*0.1)+100)    
                        else:
                            Name_Fair2.insert((l*2)+1,(int(Fare_Details.get(f"{Destination}")))+100)
                            Fair2.append((int(Fare_Details.get(f"{Destination}"))+100))
                    for e in range(2,len(Name_Fair2)+3,3):
                        Name_Fair2.insert(e,"T")      
                    z1=input()          #entering the date
                    x=z1.split("-")
                    fares1=sum(Fair2)
                    DOJ=datetime.date(int(x[-1]),int(x[-2]),int(x[-3]))    
                    file.write(f"Date of Journey:{z1}\n")
                    file.write(f"total fare=Rs.{(fares1)}\n")
                    file.write("\n")
            else:pass
        if choice==2:
            p_name=input()
            p_age=int(input())
            y=input()
            a=y.split("-")
            DOC=datetime.date(int(a[-1]),int(a[-2]),int(a[-3]))
            Interval=DOC-DOJ
            b=str(Interval).split(",")
            c=b[0].split(" ")
            d=abs(int(c[0]))#interval of days in int
            if p_age in Ages:
                P_Fair=Name_Fair[int(Name_Fair.index(p_name))+1]
                Ticket_type=Name_Fair[int(Name_Fair.index(p_name))+2]
            if p_age in Ages2:
                P_Fair=Name_Fair2[int(Name_Fair2.index(p_name))+1]
                Ticket_type=Name_Fair2[int(Name_Fair2.index(p_name))+2]
            NNOTB=0
            NNOTT=0
            if d>20:
                RA=P_Fair
                CC=P_Fair-RA
            if 20>=d>14:
                RA=P_Fair-(P_Fair*0.9)   
                CC=P_Fair-RA
            if 14>=d>7:
                RA=P_Fair-(P_Fair*0.8)
                CC=P_Fair-RA
            if 7>=d>4:
                RA=P_Fair-(P_Fair*0.5)
                CC=P_Fair-RA
            if d<=4:
                RA=0
                CC=P_Fair
            if Ticket_type=="R":
                NNOTB+=1
            if Ticket_type=="T":
                NNOTT+=1    
            RT=NOTT+NNOTT
            RR=NOTB+NNOTB 
            TC=NNOTT+NNOTB
            file.write("Remaining Seats:\n")
            file.write(f"Regular={RR}\nTatkal={RT}\nNo. of Passengers to Cancel={TC}\n")
            file.write(f"Cancelled Passengers Name={p_name}\nCancelled Passengers Age={p_age}\n")
            file.write(f"Refund Amount=Rs.{int(RA)}\nCancellation Charge=Rs.{int(CC)}\n")
        if choice==3:
            file.close()
            file1=open(r"D:\reservation.txt","r")
            re=file1.readlines()
            linelen=len(re)
            for i in range(linelen):
                print(end=re[i])
            print()    
            quit()
else:
    print("Invalid Credentials\n")