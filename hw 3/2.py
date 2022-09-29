new_file=open("C:\\Users\\Asus\\Desktop\\ghjuf\\python2\\hw\\hw 3\\students3.txt",'w')
with open("C:\\Users\\Asus\\Desktop\\ghjuf\\python2\\hw\\hw 3\\students2.txt",'r') as file2:
    all2=file2.read().split('\n')
new_line=""
with open('C:\\Users\\Asus\\Desktop\\ghjuf\\python2\\hw\\hw 3\\student.txt', 'r') as file:
    all=file.read().split('\n')
    
    for i in range(len(all)):
        for j in range(len(all2)):
            if i==j:
                new_line=str(all[i])+" "+str(all2[j])+"\n"
                new_file.write(new_line)

new_file.close()
        
        #new_lines1=str(each[0])+" "+str(each[1])+" "+str(each[2])+str(each[3])+"\n"
        
        #print(new_lines)
