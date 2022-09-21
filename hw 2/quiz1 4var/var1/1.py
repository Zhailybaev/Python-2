import math
a=int(input())
b=int(input())
c=int(input())
d=(b*b)-(4*a*c)
if d<0:
    print("no solution")
else:
    print(math.sqrt(d))
    x1=(-b-math.sqrt(d))/(2*a)
    x2=(-b+math.sqrt(d))/(2*a)
    print(x1,x2)