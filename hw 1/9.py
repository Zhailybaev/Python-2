month=input("Input the month: ")
day=input("Input the day: ")
m=int(month)
months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

i=m-1
if i==11 or i==0 or i==1:
    season="winter"
if i==2 or i==3 or i==4:
    season="spring"
if i==5 or i==6 or i==7:
    season="summer"
if i==8 or i==9 or i==10:
    season="autumn"
try:    
    print(months[m-1], day, ". Season is ", season)
except Exception as e:
    print("We have 12 months")
#for i in range(len(months)):
    