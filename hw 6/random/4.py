from random import *
s="qwertyuiopasdfghjklzxcvbnm"
s1=s.upper()
s2=s1+s
print(choices(s2,weights=None, cum_weights=None, k=5))