x=int(input("Input a dog's age in human years: "))
y=0
for i in range(x):
    if i==0 or i==1:
        y=y+10.5
    else:
        y=y+4
print("The dog's age in dog's years is", y)