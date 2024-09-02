from tkinter import *
from tkinter import messagebox
import mysql.connector

mc = mysql.connector

window = Tk()
window.geometry("1000x2000")

def login():
    u = e1.get()
    p = e2.get()

    con = mc.connect(host="localhost", user="root", password="root", database="emp")
    '''if con.is_connected():
        messagebox.showinfo("Connected", "Connected")'''

    db = con.cursor()
    query = "SELECT * FROM login WHERE name=%s AND pass=%s"
    db.execute(query, (u, p))

    result = db.fetchone()
    if result:
        messagebox.showinfo("Success", "Login successful")
    else:
        messagebox.showerror("Error", "Invalid username or password")
    
    db.close()
    con.close()


l1 = Label(window, text="Enter User Name:")
l1.pack()

e1 = Entry(window, width=20)
e1.pack()

l2 = Label(window, text="Enter Password:")
l2.pack()

e2 = Entry(window, width=20, show="*")
e2.pack()

l3 = Button(window, width=20, text="Login", font=("Arial", 12), bg="red", command=login)
l3.pack()

window.mainloop()
