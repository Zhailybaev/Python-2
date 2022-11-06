from random import *
a=list()
lucky=set()
s=""
for i in range(100):
    for x in range(10):
        a.append(randrange(1,9))
    for y in a:
        s=s+str(y)
    lucky.add(s)
    s=""
    a.clear()
luck=list(lucky)
for i in range(2):
    print(sample(luck,1))

#print(lucky)
