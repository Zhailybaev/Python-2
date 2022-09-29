import re
with open("C:\\Users\\Asus\\Desktop\\ghjuf\\python2\\hw\\hw 3\\wordlist.txt",'r') as file:
    lines=file.read().split("\n")
    m=str(lines)
    pattern3=re.findall(r'.\S*?[rstlne]\w+',m) #3)How many words contain at least one of the letters r, s, t, l, n, e
    if len(pattern3)!=0:
        print(len(pattern3))
    k=0
    for i in range(len(lines)):
        l=str(lines[i])
        
        words=l.split()
        #print(x)
        pattern1=re.findall('.\S?ime',l) #1)All words ending in ime
        if len(pattern1)!=0:
            print(pattern1)
        for x in words:
            pattern5=re.findall(r'^[b-d f-h j-n p-t v-z]+$',x) #5)All words with no vowels
            if len(pattern5)!=0:
                print("All words with no vowels:", pattern5)
            pattern2=re.findall(r'^.ave.*',x) #2)All words whose second, third, and fourth letters are ave
            if len(pattern2)!=0:
                print(pattern2)
           
        
