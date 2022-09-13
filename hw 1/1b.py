r=""
for i in range(7):
    for j in range(5):
        
        if i==0 or i==6:
            if j==1 or j==2 or j==3:
                print("*", end="")
                #r=r+"*"
            else:
                print(" ", end="")
                #r=r+" "
        if i!=0 and i!=6:
            if j==0 or j==4:
                print("*", end="")
                #r=r+"*"
            else:
                print(" ", end="")
                #r=r+" "
        
            

        
    print(end="\n") 
    r="" 