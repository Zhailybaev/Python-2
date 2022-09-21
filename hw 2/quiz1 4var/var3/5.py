print("Welcome to Hangman!")
for i in range(9):
    t=str(print("_",end=""))
print()
w="EVAPORATE"
t=list()
for i in range(9):
    t.append("_")

def func(x):
    if x not in w:
        print("Incorrect!")
    if x in w:
        for j in range(len(w)):
            if x==w[j]:
                #print(t[j])
                t[j]=x
    return t
def func2():
    for i in range(9):
        print(t[i],end="")
    print()

while "_" in t:
    x=input("Guess your letter: ")
    func(x)
    func2()
if len(t)==9:
    print("CONGRATULATIONS!")