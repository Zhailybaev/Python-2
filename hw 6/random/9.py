from random import *

s="qwertyuiopasdfghjklzxcvbnm"
t=""

def gen():
    global t
    if len(t)==5:
        return t
    x=choice(s)
    if (any(w==x for w in t))==False:
        #print(t)
        t=t+x
        return gen()
    else:
        return gen()
    
#for i in range(5):
    #x=choice(s)
#    x=gen()
#    if (any(w==x for w in t))==False:
#        print(t)
#        t=t+x
#    else:
#        gen()  
#    x=""
print(gen())