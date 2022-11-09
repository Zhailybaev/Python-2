from numpy import *
a=array([[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],
[5, 5, 5, 5, 4, 4],
[6, 6, 7, 6, 5, 5]])
r=True
#print(len(a[1]))
b=transpose(a)
print(b)
for i in range (len(b)):
    for j in range(1,len(b[0])):
        if b[i,j]<=b[i,j-1]:
            r=False
            break

print(r)
