from random import *
s="qwertyuiopasdfghjklzxcvbnm"
t=choices(s,k=5)
q=""
for x in t:
    q=q+x
print(q)
