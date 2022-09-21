
def func(x,k):
     
    if x>2*k:
        return 1
    else:
        f=x        
    return f*func(x+1,k)
n=int(input())
sum=0
for i in range(1,n+1):
    
    k=i
    sum=sum+func(i,k)
    
print(sum)