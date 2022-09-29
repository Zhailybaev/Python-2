import re
n = int(input())
output = []
for i in range(n):
    a, b = [str(x) for x in input().split()]
    pattern =r"[A-Z]+\s+[<]{1}+[a-z]+[@]{1}+[a-z]+[.]{1}+[a-z]+"
    x = re.findall(pattern, b)
    if x:
        output.append(a+" "+b[1:-1])
for j in output:
    print(j)