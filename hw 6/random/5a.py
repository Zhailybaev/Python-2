from string import *
from random import *
letters = ascii_letters
digits = digits
special_chars = punctuation
t=letters+digits+special_chars
while True:
    password = ''.join(choice(t) for i in range(10))
    if (any(c.isdigit() for c in password)
            and any(not c.isalnum() for c in password) 
            and sum(c.isupper() for c in password)>=2):
        break
print(password)