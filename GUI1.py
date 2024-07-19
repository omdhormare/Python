from tkinter import *

def square():
    n=t.get()
    n=int(n)
    s=n*n
    t1.insert(0,s)
    
window=Tk()
window.geometry("1000x1000")
window.title("Square..")

l=Label(window,text="Enter Number : ")
l1=Label(window,text="Result : ")

t=Entry(window,width="10")
t1=Entry(window,width="10")

b=Button(window,text="Square" ,command=square)
l.grid()
t.grid()

l1.grid()
t1.grid()

b.grid(row=5,column=5)
window.mainloop()