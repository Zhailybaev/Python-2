#import os
#p = os.path.abspath('student.txt ')
#print(p)
new_file=open("C:\\Users\\Asus\\Desktop\\ghjuf\\python2\\hw\\hw 3\\students2.txt",'w')
with open('C:\\Users\\Asus\\Desktop\\ghjuf\\python2\\hw\\hw 3\\student.txt', 'r') as file:
    all=file.read().split('\n')
    for student in all:
        each=student.split()
        new_lines=str(each[0].capitalize())+" "+str(each[1].capitalize())+" "+str(each[2])+" "+"301-"+str(each[3])+"\n"
        new_file.write(new_lines)
        #print(new_lines)
    
new_file.close()