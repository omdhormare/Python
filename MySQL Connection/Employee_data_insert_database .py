from tkinter import *
import mysql.connector as mc
window=Tk()

def data():
    eno=e1.get()
    name=e2.get()
    salary=e3.get()
    
    con=mc.connect(host="localhost",user="root",password="root",database="employee")
    db=con.cursor()
    #db.execute("create database employee")
    #db.execute(""" CREATE TABLE IF NOT EXISTS emp ( eno VARCHAR(10) PRIMARY KEY,ename VARCHAR(20),sal VARCHAR(20))""")
    db.execute("INSERT INTO emp (eno, ename, sal) VALUES (%s, %s, %s)", (eno, name, salary))
    con.commit()

window.geometry("1500x1500")
window.title("Employee Management System")

l1=Label(text="Employee Management System",font=("arial",20))
l1.pack()

l1=Label(window,text="Enter Employee No : ",font=("arial",10))
l1.pack()

e1=Entry(window,width="30",font=("arial",10))
e1.pack()

l2=Label(window,text="Enter Employee Name : ",font=("arial",10))
l2.pack()

e2=Entry(window,width="30",font=("arial",10))
e2.pack()

l3=Label(window,text="Enter Employee Salary : ",font=("arial",10))
l3.pack()

e3=Entry(window,width="30",font=("arial",10))
e3.pack()

b=Button(window,text="insert Record ",font=("arial",10),width=30,command=data)
b.pack()
window.mainloop()