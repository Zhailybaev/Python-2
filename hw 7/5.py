from string import *
class Password():
    def __init__(self,p1, p2, p3):
        self.p1=p1
        self.p2=p2
        self.p3=p3
    def part_1(self):
        passw1=""
        passw1=f"{ord(self.p1[0])-96}"+self.p1[1]+f"{ord(self.p1[2])-96}"
        return passw1
    def part_2(self):
        passw2=self.p2[::-1]
        return passw2
    def part_3(self):
        passw3=""
        for i in range(len(self.p3)):
            if self.p3[i]!="z":
                m=ord(self.p3[i])+1
                x=chr(m)
                #print(x)
                passw3=passw3+x
                #print(passw3)
            else:
                x=chr(97)
                passw3=passw3+x
        return passw3

s="mubashirh"
if not s.islower() or len(s)!=9:
    print("BANG! BANG! BANG!")
else:

    p1=s[0]+s[1]+s[2]
    p2=s[3]+s[4]+s[5]
    p3=s[6]+s[7]+s[8]

    p=Password(p1,p2,p3)
    password=p.part_2()+p.part_3()+p.part_1()

    print(password)

