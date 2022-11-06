from string import *
import secrets
letters = ascii_letters
digits = digits
#special_chars = punctuation
t=letters+digits
while True:
    password = ''.join(secrets.choice(t) for i in range(10))
    if (sum(c.isdigit() for c in password)>=4):
        break
print(password)