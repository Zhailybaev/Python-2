a=list()
b=list()
for i in range(6):
    x=int(input())
    a.append(x)
for i in range(len(a)):
    if a[i]%2==1:
        b.append(a[i])
b.sort()
if len(b)==0:
    print("not found")
else:
    print(b[0])