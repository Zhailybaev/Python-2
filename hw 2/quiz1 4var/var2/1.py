import random
x=random.randrange(1,100)
print("Numbers:", x)
def func(a):
    if a>x:
        print("The number is fewer")
    if a<x:
        print("The number is more")
    if a==x:
        print("BINGO")
a=int(input("Guess: "))
func(a)
b=int(input("Guess: "))
func(b)
c=int(input("Guess: "))
func(c)

