import re
n=int(input())
for i in range(n):
    s=str(input())
    pattern=re.findall(r"[A-Z]+[<]{1}+[a-z]+[@]{1}+[a-z]+[.]{1}+[a-z]+",s)
    if len(pattern)!=0:

        pat=re.sub("<","",s)
#pat=re.findall(r'[A-Z]+[a-z]+[@.]{1}+[a-z]+',s)
        pat2=re.sub(">","",pat)
        print(pat)

