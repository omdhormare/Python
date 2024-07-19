from tkinter import *

def color():
    window.configure(bg='red')
def color1():
    window.configure(bg='blue')

window=Tk()
window.title("Hii Python...")
window.geometry("2000x2000")
button=Button(window,text="Red Color",height=5,width=15,command=color)
button1=Button(window,text="Blue Color",height=5,width=15,command=color1)

button.grid()
button1.grid()
window.mainloop()
