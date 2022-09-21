import math
y1=int(input("UP "))
y2=int(input("DOWN "))
x1=int(input("LEFT "))
x2=int(input("RIGHT "))

y=-y2
x=-x1
a=y+y1
b=x+x2
c=math.sqrt(a*a+b*b)
print(int(c))