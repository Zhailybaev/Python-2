s=str(input())
t=s.lower()
for i in range(len(t)):
    if t[i]!=" ":
        print(ord(t[i])-96, end=" ")