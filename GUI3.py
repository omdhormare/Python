from tkinter import *
window=Tk()
window.geometry("1000x1000")
window.config(bg="black")
title=Label(window,text="Hello Python",font=("times new roman",50,"underline"),
bg="orangered").pack(fill="x")

window.mainloop()