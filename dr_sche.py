# بسم الله الرحمن الرحيم

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter import ttk
import pymysql
import mysql.connector


# Database connection
def connect_database():
    try:
        # The Connection method of MySQL
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Q,u5.S@2',
            port='3306',
            database='doctor_table'
        )
        # A pointer
        my_cursor = mydb.cursor()
    except:
        messagebox.showerror('ERROR', 'Database Connectivity Issue, Please Try Again.')
        return

    q = 'SELECT * FROM nurse_sche WHERE status=%s'
    my_cursor.execute(q, ('Accepted', ))
    rows = my_cursor.fetchall()
    for data in rows:
        my_tree.insert(parent='', index='end', text='', values=(data[0], data[1], data[2]))
    mydb.commit()
    mydb.close()


# GUI design.
root = Tk()
root.title("Appointments")
root.resizable(False, False)
root.geometry('700x300')
root.config(background='white')

# Treeview design.
my_tree = ttk.Treeview(root)
style = ttk.Style()
style.theme_use('clam')
style.configure('Treeview.Heading', background="green3")
vsb = ttk.Scrollbar(root, orient="vertical", command=my_tree.yview)
vsb.place(x=638, y=77, height=173)
my_tree.configure(yscrollcommand=vsb.set)

# Define our columns.
my_tree['columns'] = ('Day', 'Time', 'Status')

# Format our columns.
my_tree.column('#0', width=0, stretch=NO)
my_tree.column('Day', anchor=W, width=200)
my_tree.column('Time', anchor=CENTER, width=200)
my_tree.column('Status', anchor=W, width=200)


# Create headings
my_tree.heading('#0', text='', anchor=W)
my_tree.heading('Day', text='Day', anchor=W)
my_tree.heading('Time', text='Time', anchor=W)
my_tree.heading('Status', text='Status', anchor=W)
my_tree.pack(pady=50)

connect_database()

root.mainloop()