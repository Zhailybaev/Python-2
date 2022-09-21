import math
x=int(input())
y=int(input())
try:
    z=math.sqrt(x-math.sqrt(y))
    print(z)
except Exception as e:
    print("plz enter valid numbers")