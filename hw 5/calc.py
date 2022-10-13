from tkinter import *
#from math import *
from numpy import *
import re
top=Tk()
string1=""
string2=""
def show(string1):
    output = Label(top, text = string1, width = 30, height = 2)
    output['bg']= "white"
    output.grid(row = 0, column=0, columnspan=7)
def click(x):
    global string1, string2
    if x=="CE":
        string1=""
        string2=""
        show(string1)
    if x=="7":
        string1+="7"
        string2+="7"
        show(string1)
    if x=="8":
        string1+="8"
        string2+="8"
        show(string1)
    if x=="9":
        string1+="9"
        string2+="9"
        show(string1)
    if x=="0":
        string1+="0"
        string2+="0"
        show(string1)
    if x=="1":
        string1+="1"
        string2+="1"
        show(string1)
    if x=="2":
        string1+="2"
        string2+="2"
        show(string1)
    if x=="3":
        string1+="3"
        string2+="3"
        show(string1)
    if x=="4":
        string1+="4"
        string2+="4"
        show(string1)
    if x=="5":
        string1+="5"
        string2+="5"
        show(string1)
    if x=="6":
        string1+="6"
        string2+="6"
        show(string1)
    if x=="+":
        string1+="+"
        string2+="+"
        show(string1)
    if x=="-":
        string1+="-"
        string2+="-"
        show(string1)
    if x=="/":
        string1+="/"
        string2+="/"
        show(string1) 
    if x=="x":
        string1+="x"
        string2+="*"
        show(string1)
    if x=="e":
        string1+="e"
        string2+="e"
        show(string1)  
    if x=="√":
        string1+="√("
        string2+="sqrt("
        show(string1)
    if x=="(":
        string1+="("
        string2+="("
        show(string1)
    if x==")":
        string1+=")"
        string2+=")"
        show(string1)
    if x=="%":
        string1+="%"
        string2+="/100"
        show(string1)
    if x==",":
        string1+=","
        string2+="."
        show(string1)
    if x=="ln(":
        string1+="ln("
        string2+="log("
        show(string1)
    if x=="log(":
        string1+="log("
        string2+="log("
        show(string1)
    if x=="x²":
        t = re.findall("[0-9]+$", string1)
        string1+= "²"
        string2=string2+"*"+ t[0]
        print(t)
        show(string1)
    if x=="sin(":
        t = re.findall("[0-9]+,?+$", string1)
        i=int(t[0])
        s=sin(i)
        #print(s)
        string2=str(s)
    if x=="tg(":
        t = re.findall("[0-9]+$", string1)
        i=int(t[0])
        s=tan(i)
        string2=str(s)
    if x=="ctg(":
        t = re.findall("[0-9]+$", string1)
        i=int(t[0])
        s=1/tan(i)
        string2=str(s)
    if x=="cos(":
        t = re.findall("[0-9]+$", string1)
        i=int(t[0])
        s=cos(i)
        string2=str(s)
    if x=="=":
        try: eval(string2)
        except: print(show("Error"))
        else:
            tmp = int(eval(string2)) if eval(string2) - int(eval(string2)) == 0.0 else eval(string2) # to avoid 4.0 
            show(tmp)
            string1= str(tmp)
            string2 = string1
    top.mainloop()

B=Button(top, font=('courier',10), text='%', width=4,height=2, command=lambda: click('%')).grid(row=1, column=1)
B=Button(top, font=('courier',10), text='(', width=4,height=2, command=lambda: click('(')).grid(row=1, column=3)
B=Button(top, font=('courier',10), text=')', width=4,height=2, command=lambda: click(')')).grid(row=1, column=4)
B=Button(top, font=('courier',10), text='CE', width=4,height=2, command=lambda: click('CE')).grid(row=1, column=5)
B=Button(top, font=('courier',10), text='7', width=4,height=2, command=lambda: click('7')).grid(row=2, column=2)
B=Button(top, font=('courier',10), text='8', width=4,height=2, command=lambda: click('8')).grid(row=2, column=3)
B=Button(top, font=('courier',10), text='9', width=4,height=2, command=lambda: click('9')).grid(row=2, column=4)
B=Button(top, font=('courier',10), text='4', width=4,height=2, command=lambda: click('4')).grid(row=3, column=2)
B=Button(top, font=('courier',10), text='5', width=4,height=2, command=lambda: click('5')).grid(row=3, column=3)
B=Button(top, font=('courier',10), text='6', width=4,height=2, command=lambda: click('6')).grid(row=3, column=4)
B=Button(top, font=('courier',10), text='1', width=4,height=2, command=lambda: click('1')).grid(row=4, column=2)
B=Button(top, font=('courier',10), text='2', width=4,height=2, command=lambda: click('2')).grid(row=4, column=3)
B=Button(top, font=('courier',10), text='3', width=4,height=2, command=lambda: click('3')).grid(row=4, column=4)
B=Button(top, font=('courier',10), text='0', width=4,height=2, command=lambda: click('0')).grid(row=5, column=3)
B=Button(top, font=('courier',10), text='x²', width=4,height=2, command=lambda: click('x²')).grid(row=2, column=1)
B=Button(top, font=('courier',10), text='√', width=4,height=2, command=lambda: click('√')).grid(row=3, column=1)
B=Button(top, font=('courier',10), text='log(', width=4,height=2, command=lambda: click('log(')).grid(row=4, column=1)
B=Button(top, font=('courier',10), text='ln(', width=4,height=2, command=lambda: click('ln(')).grid(row=5, column=2)
B=Button(top, font=('courier',10), text=',', width=4,height=2, command=lambda: click(',')).grid(row=5, column=4)
B=Button(top, font=('courier',10), text='x', width=4,height=2, command=lambda: click('x')).grid(row=3, column=5)
B=Button(top, font=('courier',10), text='-', width=4,height=2, command=lambda: click('-')).grid(row=4, column=5)
B=Button(top, font=('courier',10), text='+', width=4,height=2, command=lambda: click('+')).grid(row=5, column=5)
B=Button(top, font=('courier',10), text='=', width=4,height=2, command=lambda: click('=')).grid(row=6, column=5)
B=Button(top, font=('courier',10), text='e', width=4,height=2, command=lambda: click('e')).grid(row=5, column=1)
B=Button(top, font=('courier',10), text='sin(', width=4,height=2, command=lambda: click('sin(')).grid(row=6, column=1)
B=Button(top, font=('courier',10), text='cos(', width=4,height=2, command=lambda: click('cos(')).grid(row=6, column=2)
B=Button(top, font=('courier',10), text='tg(', width=4,height=2, command=lambda: click('tg(')).grid(row=6, column=3)
B=Button(top, font=('courier',10), text='ctg(', width=4,height=2, command=lambda: click('ctg(')).grid(row=6, column=4)
B=Button(top, font=('courier',10), text='/', width=4,height=2, command=lambda: click('/')).grid(row=2, column=5)

output = Label(top, text = string1, width = 30, height = 2)
output['bg']= "white"
output.grid(row = 0, column = 0, columnspan = 7)
top.mainloop()