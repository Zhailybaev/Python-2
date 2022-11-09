from numpy import *

class Sudoku():
    def __init__(self,s):
        self.s=s
    
    def board(self):
        b=list()
        t=self.s
        for i in range(9):
            a=list()
            for j in range(9):
                a.append(t[j])
            b.append(a)
            t=t[9:]
        ar=array(b)
        a.clear()
        b.clear()
        
        return ar
    def board1(self):
        b=list()
        t=self.s
        for i in range(27):
            a=list()
            for j in range(3):
                a.append(t[j])
            b.append(a)
            t=t[3:]
        return b
    def get_row(self,x):
        arr=Sudoku.board(self)
        return arr[x]
    def get_col(self,x):
        arr=transpose(Sudoku.board(self))
        return arr[x]

    def get_sqr(self,l):
        b=Sudoku.board1(self)
        c=list()
        d=list()
        if len(l)==1:
            
            for j in range(3):
                if l[0]<3:
                    c.append(b[l[0]+3*j])
                if l[0]>=3 and l[0]<6:
                    c.append(b[l[0]+3*j+6])
                if l[0]>=6 and l[0]<9:
                    c.append(b[l[0]+3*j+12])
            
        if len(l)!=1:
           
            for j in range(3):
                if l[0]<3:
                    if l[1]>=6 and l[1]<=8:
                        c.append(b[2+3*j])
                    if l[1]>=3 and l[1]<=5:
                        c.append(b[1+3*j])
                    if l[1]>=0 and l[1]<=2:
                        c.append(b[3*j])
                if l[0]>=3 and l[0]<6:
                    if l[1]>=6 and l[1]<=8:
                        c.append(b[2+3*j+9])
                    if l[1]>=3 and l[1]<=5:
                        c.append(b[3*j+10])
                    if l[1]>=0 and l[1]<=2:
                        c.append(b[3*j+9])
                if l[0]>=6 and l[0]<9:
                    if l[1]>=6 and l[1]<=8:
                        c.append(b[2+3*j+18])
                    if l[1]>=3 and l[1]<=5:
                        c.append(b[3*j+19])
                    if l[1]>=0 and l[1]<=2:
                        c.append(b[3*j+18])
        for x in c:
                for y in x:
                    d.append(int(y))        
        return d
s="417950030000000700060007000050009106800600000000003400900005000000430000200701580"
game=Sudoku(s)
arr=game.board()
#print(arr)
#print(game.get_row(0))
#print(game.get_col(8))
#print(game.board1())
print(game.get_sqr([8,3]))

            
