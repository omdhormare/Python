from tkinter import *
from tkinter import messagebox
import mysql.connector as mc
def login():
    u=e1.get()
    p=e2.get()
    con=mc.connect(host="localhost",username="root",password="root",database="student")
    db=con.cursor()
    #db.execute("create database student")
    #db.execute("create table login(username varchar(20),password varchar(20))")
    #db.execute("insert into login values('om',123)")
    db.execute("select * from login where username=%s and password=%s",(u,p))
    res=db.fetchall()
    if res:
        messagebox.showinfo("Login","Succefully Login")
    else:
        messagebox.showerror("Invalid login","wrong password")
    con.commit()
    
    
window=Tk()
window.title("Student Login...")
window.geometry("1000x1000")
l1=Label(text="Student Login..",font=("arial",30))
l1.pack()

l2=Label(window,text="Enter User Name : ")
l2.pack()

e1=Entry(window,width=20)
e1.pack()

l3=Label(window,text="Enter Password : ")
l3.pack()

e2=Entry(window,width=20,show="*")
e2.pack()

b=Button(window,text="Login",width=20,command=login)
b.pack()
window.mainloop()