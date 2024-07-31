from tkinter import *

window = Tk()
window.geometry("1000x1000")
def add():
    a=int(e1.get())
    b=int(e2.get())
    e3.delete(0,END)
    e3.insert(0,a+b)
    
def sub():
    a=int(e1.get())
    b=int(e2.get())
    e4.delete(0,END)
    e4.insert(0,a-b)   

def mul():
    a=int(e1.get())
    b=int(e2.get())
    e5.delete(0,END)
    e5.insert(0,a*b)   
    
def div():
    a=int(e1.get())
    b=int(e2.get())
    e6.delete(0,END)
    e6.insert(0,a/b)      
       
l1=Label(window,text="Enter 1 No : ")
l1.pack()

e1=Entry(window,width="20")
e1.pack()

l2=Label(window,text="Enter 2 No : ")
l2.pack()

e2=Entry(window,width="20")
e2.pack()

l3=Label(window,text="Addtion : ")
l3.pack()

e3=Entry(window,width="20")
e3.pack()

l4=Label(window,text="Substraction : ")
l4.pack()

e4=Entry(window,width="20")
e4.pack()

l6=Label(window,text="Division : ")
l6.pack()

e6=Entry(window,width="20")
e6.pack()

l5=Label(window,text="Multiplication : ")
l5.pack()


e5=Entry(window,width="20")
e5.pack()


r1 = Radiobutton(window, text="Add", value=1, font=("Arial", 10),command=add)
r1.pack()

r2=Radiobutton(window,text="Substraction", value=2,font=("Arial",10),command=sub)
r2.pack()

r3=Radiobutton(window,text="Multiplication", value=3,font=("Arial",10),command=mul)
r3.pack()

r4=Radiobutton(window,text="Division", value=4,font=("Arial",10),command=div)
r4.pack()
window.mainloop()
