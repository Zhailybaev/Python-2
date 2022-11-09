from numpy import *
lst = [
  [1, 2, 3, 7 ],
  [4, 5, 6, 15],
  [7, 8, 9, 24],
  [12,15,18,45]
]
a=array([
  [1, 2, 3, 6 ],
  [4, 5, 6, 15],
  [7, 8, 9, 24],
  [12,15,18,45]
])
sum=0
sum1=0
b=list()
c=list()
for i in range (4):
    for j in range(4):
        if j!=3 :
            sum=sum+a[i,j]
            sum1=sum1+a[j,i]
    b.append(sum)
    c.append(sum1)
    sum=0
    sum1=0
l=5
m=5
n=0
for j in range(4):
    if c[j]==a[3,j] and b[j]==a[j,3]: 
        n=n+1   
    else:        
        if c[j]!=a[3,j] :
            l=j
            
        if b[j]!=a[j,3]:
            m=j
            
    if l!=5 and m!=5:
        p=a[m,l]
        print("wrong number:",a[m,l])
        d=c[l]-a[3,l]
        print(d , c[l])
        if d>0:
            a[m,l]=p-d    
        else:
            a[m,l]=p+d    
        print(a)
        m=5
        l=5
if n==4:
    print("everything is right")