def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)


n=int(input())
c=fact(n)
#print(fact(n))

sum=3
for i in range(3,n+1):
    sum=sum+i*2*fact(i)
    
print(sum)