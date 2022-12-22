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

    # Here, there is an intermediate to have a link with pat_reserve and have two values 0, 1
    query = 'SELECT * FROM pat_reserve WHERE selected=%s'
    my_cursor.execute(query, (1, ))
    row = my_cursor.fetchone()
    my_tree.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], row[5]))
    q = 'UPDATE pat_reserve SET selected=%s WHERE name=%s'
    my_cursor.execute(q, (0, row[0]))
    mydb.commit()
    mydb.close()


# GUI design.
root = Tk()
root.title("Time Schedule")
root.resizable(False, False)
root.geometry('900x300')
root.config(background='white')

# Treeview design.
my_tree = ttk.Treeview(root)
style = ttk.Style()
style.theme_use('clam')
style.configure('Treeview.Heading', background="green3")

# Define our columns.
my_tree['columns'] = ('name', 'bod', 'gender', 'pain', 'day', 'time')

my_tree.column('#0', width=0, stretch=NO)
my_tree.column('name', anchor=W, width=150)
my_tree.column('bod', anchor=CENTER, width=100)
my_tree.column('gender', anchor=CENTER, width=100)
my_tree.column('pain', anchor=CENTER, width=350)
my_tree.column('day', anchor=CENTER, width=100)
my_tree.column('time', anchor=W, width=50)

# Create headings
my_tree.heading('#0', text='', anchor=W)
my_tree.heading('name', text='Name', anchor=W)
my_tree.heading('bod', text='BOD', anchor=CENTER)
my_tree.heading('gender', text='Gender', anchor=CENTER)
my_tree.heading('pain', text='Pain', anchor=CENTER)
my_tree.heading('day', text='Day', anchor=CENTER)
my_tree.heading('time', text='Time', anchor=W)
my_tree.pack(pady=50)

connect_database()


root.mainloop()