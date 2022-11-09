from numpy import *

def change(a):
    s=list()
    b=list()
    for x in a:
        for i in x:
            s.append(int(i))
    for i in range(3):
        t=list()
        for j in range(3):
            t.append(s[j])
        b.append(t)
        s=s[3:]
    arr=array(b)            
    return arr

a=array([
  ("001"),
  ("002"),
  ("003")
])

arr=change(a)
#print(type(arr))
k=0
for i in range(len(a)):
    for j in range(len(a[0])):
        if i<len(a)-1 :
            if arr[i][j]<arr[i][j+1]:
                k=k+1
        if j<len(a[0])-1:
            if arr[i][j]<arr[i+1][j]:
                k=k+1
        if j<len(a[0])-1 and i<len(a)-1:
            if arr[i][j]<arr[i+1][j+1]:
                k=k+2
print(k)

