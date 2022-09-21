s=input()
t=s[len(s)-1]
for i in range(len(s)):
    if i!=len(s)-1:
        t=t+s[i]
print(t)