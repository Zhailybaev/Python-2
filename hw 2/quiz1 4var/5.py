s=str(input())
t=str(input())
d=dict()
f=dict()
for i in range(len(s)):
    if s[i] in d.keys():
        d[s[i]]+=1
    else:
        d[s[i]]=1
    if t[i] in f.keys():
        f[t[i]]+=1
    else:
        f[t[i]]=1
r=""
if len(d)!=len(f):
    print("not encoded")
else:
    v=list(d.keys())
    u=list(f.keys())
    for i in range(len(v)):
        if d[v[i]]==f[u[i]] and v[i]==u[i]:
            r="not encoded"
        else:
            r="YES"
    

    print(r)

