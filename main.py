from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i)

def search():
    q2 = q.get()
    query= "SELECT id, first_name, last_name, age FROM customers WHERE first_name LIKE '%"+q2+"%' OR last_name LIKE '%"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)


mydb = mysql.connector.connect(host="localhost",user="root", password="root", database="sample", auth_plugin="mysql_native_password")
cursor = mydb.cursor() 

root = Tk()
q = StringVar()
wrapper1 = LabelFrame(root, text="Customer List")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Customer Data")



wrapper1.pack(fill="both", expand="yes", padx=20, pady=10 )
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10 )
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10 )

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4), show="headings", height="6")
trv.pack()

trv.heading(1, text="Customer ID")
trv.heading(2, text="First Name")
trv.heading(3, text="Last Name")
trv.heading(4, text="Age")

query = "SELECT id, first_name, last_name, age from customers"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

#area ricerca
lbl = Label(wrapper2, text="Search")
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper2, text="Search", command=search)
btn.pack(side=tk.LEFT, padx=6)



root.title("Applicazione")
root.geometry("800x700")
root.mainloop()


