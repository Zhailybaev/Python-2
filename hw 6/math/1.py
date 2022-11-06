from math import *
def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def qwe(n):
    for a in range(1,13):
        for b in range(1,8):

            if a*a+b*b==n:
                return a,b

#def sum(s):
    
#    sum1=sum1+s
#    return sum(sum1)
k=0
n=4*k+1
sum_a=0
sum_b=0
for k in range(1,38):
    n=4*k+1
    #print(n)
    
    if IsPrime(n)==True:
        #print(n)
        s_a=qwe(n)[0]
        sum_a=sum_a+s_a
        s_b=qwe(n)[1]
        sum_b=sum_b+s_b
print(sum_a)
print(sum_b)

