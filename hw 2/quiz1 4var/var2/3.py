d=dict()
s=str(input())
for i in range(len(s)):
    if s[i] in d.keys():
        d[s[i]]+=1
    else:
        d[s[i]]=1
print(d)