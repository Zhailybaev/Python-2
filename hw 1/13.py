import datetime
y=int(input("Input a year: "))
m=int(input("Input a month [1-12]: "))
d=int(input("Input a day [1-31]: "))
if m==12 and d==31:
    x=datetime.datetime(y+1,m-11,d-30)
if m==2 and y%4==0 and d==28:
    x=datetime.datetime(y,m+1,1)
if m==2 and y%4!=0 and d==29:
    x=datetime.datetime(y,m+1,1)
if m==4 or m==6 or m==9 or m==11:
    if d==30:
        x=datetime.datetime(y,m+1,1)
if m!=4 and m!=6 and m!=9 and m!=11 and m!=12:
    if d==31:
        x=datetime.datetime(y,m+1,1)
    else:
        x=datetime.datetime(y,m,d+1)
print(x)