s=str(input())
def find(x):
    a=list()
    for i in range(len(s)):
        if s[i]==x:
            a.append(i)
    return a

x=input()
print(find(x))