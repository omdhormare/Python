#Addtion of Two Number Using Tkinter
from tkinter import *

def Add():
    a=t.get()
    b=t1.get()
    b=int(b)
    a=int(a)
    t2.delete(0,END)
    t2.insert(0,a+b)
def sub():
    a=t.get()
    b=t1.get()
    b=int(b)
    a=int(a)
    t2.delete(0,END)
    t2.insert(0,a-b)
def mul():
    a=t.get()
    b=t1.get()
    b=int(b)
    a=int(a)
    t2.delete(0,END)
    t2.insert(0,a*b)
def div():
    a=t.get()
    b=t1.get()
    b=int(b)
    a=int(a)
    t2.delete(0,END)
    t2.insert(0,a/b)
                
window=Tk()

window.geometry("1000x1000")
window.config(bg="black")
window.title("Addtion program..")
t=Label(window,text="Calculate").pack()
l=Label(window,text="Enter 1 Number : ")
l1=Label(window,text="Enter 2 Number : ")

l2=Label(window,text="Result : ")


t=Entry(window,width=20)
t1=Entry(window,width=20)
t2=Entry(window,width=20)

b=Button(window,text="Addtion", command=Add)
b1=Button(window,text="Substraction", command=sub)
b2=Button(window,text="Multiplication", command=mul)
b3=Button(window,text="Division", command=div)


l.grid(row=0, column=0, padx=10, pady=5)
t.grid(row=0, column=1, padx=10, pady=5)

l1.grid(row=1, column=0, padx=10, pady=5)
t1.grid(row=1, column=1, padx=10, pady=5)

l2.grid(row=2, column=0, padx=10, pady=5)
t2.grid(row=2, column=1, padx=10, pady=5)

b.grid(row=3, column=0, padx=10, pady=5)
b1.grid(row=3, column=1, padx=10, pady=5)
b2.grid(row=4, column=0, padx=10, pady=5)
b3.grid(row=4, column=1, padx=10, pady=5)

window.mainloop()