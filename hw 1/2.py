r=""
for i in range(7):
    for j in range(5):
        if j==0:
            r=r+"*"
        
        if i==0 or i==3:
            if j<4 and j!=0:
                r=r+"*"  
            
        if i==1 or i==2:
            if j==3:
                r=r+"*"
            else:
                r=r+" "
        if i==5:
            if j==2:
                r=r+"*"      
            else:
                r=r+" "  
        
        if i==4:
            if j==1:
                r=r+"*"
            else:
                r=r+" "  
        
        if i==6:
            if j==3:
                r=r+"*"
            else:
                r=r+" "    
   
    print(r) 
    r="" 