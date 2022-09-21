def sum(a,b,c):
    f=a*a*a+b*b*b+c*c*c
    return f
for i in range(100,1000):
    a=int(i/100)
    b=int(i/10)%10
    c=i%10
    s=str(a)+str(b)+str(c)
    #sum(a,b,c)
    if int(s)==sum(a,b,c):
        print(int(s))

        