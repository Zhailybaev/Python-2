from numpy import *
l=list()
def sort(b):
    c=list()
    for x in b:
        if x not in c:
            c.append(x)
    for i in range(len(c)):
        for j in range(2):
            if i+1<len(c)-1 and c[i][0]==c[i+1][0]:
                c.pop(i)
    return c
def freq_count(a,n,m=0):
    global l
    k=0
    r=list()
   
    for i in range(len(a)):
        if type(a[i])==int:
            if a[i]==n:
                k=k+1
        if type(a[i])==list:
            r=r+a[i]  
        if i==len(a)-1:
            l.append([m,k])
            m=m+1
        if m!=0:
            freq_count(r,n,m)
    return l
                  
a=array([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]])
k=0
b=freq_count(a,2)

print(sort(b))
      

