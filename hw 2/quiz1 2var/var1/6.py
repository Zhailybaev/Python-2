s=str(input())
t=str(input())
k=0
for i in range(len(s)):
    if s[i] in t:
        k=k+1
if k==len(s):
    print("True")
else:
    print("False")
