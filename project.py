from tkinter import *
import numpy as np
from sympy import *
from scipy import *
from tkinter import messagebox as mb
from tkinter import ttk

windows=[]

window = Tk()
window.title("Matrix")
window.geometry("700x400")
window.configure(bg='bisque2')
window.resizable(False, False)

windows.append(window)

# empty arrays for your Entrys and StringVars
text_var = []
entries = []

class Display():
    def __init__(self,a,x3,y3):
        self.a=a
    def go_back(self, cur_window):
        cur_window.withdraw()
        window.deiconify()
    def view(self,window_solve,matr,x3,y3):
        n=len(matr)
        pr=x3
        for i in range(n):
            for j in range(n):
                Label(window_solve, text=f'{matr[i][j]}').place(x=60 + x3, y=50 + y3)
                
                x3+=30
            y3 += 20
            x3 = pr
        if n==4:
            for k in range(4):
                if x3!=0 and x3!=30 and x3!=140  and x3!=1160:
                    print(x3)
                    Label(window_solve, text='->').place(x=200+x3, y=75)
        if n==3:
            for k in range(4):
                if x3!=0 and x3!=30 and x3!=140 and x3!=160 and x3!=410:
                    print(x3)
                    Label(window_solve, text='->').place(x=165+x3, y=70)
        if n==2:
            print(x3)
            
            Label(window_solve, text='->').place(x=85, y=70)
        
def closing():
    answer = mb.askyesno(
        title = "Closing", 
        message = "Are you sure you want to leave?\nEntered data will not be saved.")
    if answer:
        for w in windows:
            w.destroy()
def go_back(window,cur_window):
        cur_window.withdraw()
        window.deiconify()
        window.protocol("WM_DELETE_WINDOW", closing)

w=[]   
def swap(a,k,w):
    n=len(a)
    for i in range (k,n):
        for j in range(n):
        
            if i+1!=n:
                a[i][j]=a[i+1][j]
                a[i+1][j]=w[j]
    return a

def ref(window,a):
    window.withdraw()
    window_solve = Tk()
    window_solve.title('Solving')
    window_solve.geometry('600x400')
    window_solve.configure(bg='bisque2')
    windows.append(window_solve)
    n=len(a)
    x3=-40
    y3=0
    d=Display(a,x3,y3)
    d.view(window_solve,a,x3,y3)
    x3+=n*50
    L = np.zeros((n,n))
    np.fill_diagonal(L,1)
    Label(window_solve, text='REF').place(x=20 , y=30)
    b=np.zeros((n,n))
    Label(window_solve,text='Notes\n 1.Under -> you can see coefficient(k), it means\n the lower row=previous l.r. -k*pivot.\n 2.Check L*U means L-matrix * U-matrix.').place(x=340,y=160)
    for i in range(n):
        b=a
        for j in range(i+1, n):
            if a[i][i]!=0:
                ratio = np.round(a[j][i]/a[i][i],2)
                L[j][i]=ratio
                a[j]=(a[j]- ratio * a[i])
                Label(window_solve, text=f'{ratio}').place(x=10+x3 , y=50)
                print(a)
            else:
              w=tuple(a[i])
              swap(a,i,w)
            if a.all()==b.all():
                d.view(window_solve,a,x3,y3)
                x3+=(n)*50
    Label(window_solve, text='L =').place(x=30 , y=180)
    x3=0
    y3=110
    d.view(window_solve,L,x3,y3)
    Label(window_solve, text='U =').place(x=190 , y=180)
    x3=160
    y3=110
    d.view(window_solve,a,x3,y3)
    Button(window_solve,text="Back", bg='bisque3', width=15, command=lambda : go_back(window,window_solve)).place(x=300,y=300)
    Label(window_solve, text="CHECK LxU:").place(x=30, y=250)
    lu=np.matmul(L,a)
    x3=30
    y3=240
    d.view(window_solve, lu,x3,y3)
    window_solve.mainloop()

n=2
rows, cols = [n,n]
class Present():
  def __init__(self,n):
    self.n=n
  def rc_add(self): #get number of rows and columns
    self.n+=1
    return Present.pres_matr(self)
  def rc_min(self):
    if self.n!=2:
      self.n=self.n-1
      return Present.pres_matr(self)
  def pres_matr(self):
    n=self.n
    x2 = 0
    y2 = 0
    Label(window,text=f'{n} x {n}',bg="bisque2").place(x=120, y=20)
    
    for i in range(n):
      text_var.append([])
      entries.append([])
      for j in range(n):
        # append your StringVar and Entry
        text_var[i].append(StringVar(value='0'))
        
        entries[i].append(Entry(window, textvariable=text_var[i][j],width=3))
        entries[i][j].place(x=60 + x2, y=50 + y2)
        
        x2 += 30
      y2 += 30
      x2 = 0
    entries.clear()
  def get_mat(self,window):
    matrix = []
    for i in range(self.n):
        matrix.append([])
        for j in range(self.n):
            matrix[i].append(int(text_var[i][j].get()))
    a=np.array(matrix, dtype=float)
    ref(window,a)


Label(window, text="Enter matrix :", font=('arial', 10, 'bold'), 
      bg="bisque2").place(x=20, y=20)



p=Present(n)
p.pres_matr()

Button(window,text="Submit", bg='bisque3', width=15, command= lambda: p.get_mat(window)).place(x=160,y=250)
Button(window,text="+",bg='bisque3', width=10, command= lambda: p.rc_add()).place(x=60,y=200)
Button(window,text="-",bg='bisque3', width=10, command=lambda: p.rc_min()).place(x=190,y=200)
Label(window, text="Notes\n 1. Enter a number(you are not allowed to enter string,char etc.)\n 2. You can change dimension(dim) your matrix by using +- (you can see dim near Enter...)\n 3. max-size=4 and min-size=2").place(x=220, y=40)

window.protocol("WM_DELETE_WINDOW", closing)
window.mainloop()