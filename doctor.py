# بسم الله الرحمن الرحيم

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry
import pymysql
import mysql.connector


def imp_log():
    root.destroy()
    import login


def imp_report():
    if dia_entry.get() == '' or pre_entry.get(0.0, END) == '' or cal_entry.get() == '' or tst_entry.get() == '':
        messagebox.showerror('Warning ;)', 'Oh, You forgot to fill a field')
    else:
        import dr_report


def imp_sche():
    import dr_sche


def clear():
    tst_entry.delete(0, END)
    dia_entry.delete(0, END)
    pre_entry.delete(0.0, END)
    cal_entry.delete(0, END)


# Insertion of data in the patient profile
def insertion(row):
    pat_entry.insert(0, row[0])
    phone_entry.insert(0, row[7])
    pain_entry.insert(0, row[3])
    disabled()


# After insertion, These fields become readonly.
def disabled():
    pat_entry.config(state=DISABLED)
    phone_entry.config(state=DISABLED)
    pain_entry.config(state=DISABLED)


# Database connection
def connect_database():
    if dia_entry.get() == '' or pre_entry.get(0.0, END) == '' or cal_entry.get() == '' or tst_entry.get() == '':
        messagebox.showerror('Warning ;)', 'Oh, You forgot to fill a field')
    else:
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

        query = 'INSERT INTO dr_diagnose(name, phone, diagnose, prescription, test, diagnose_date, selected) VALUES(%s,%s,%s,%s,%s,%s,%s)'
        my_cursor.execute(query, (pat_entry.get(), phone_entry.get(), dia_entry.get(), pre_entry.get(0.0, END),
                                  tst_entry.get(), cal_entry.get(), 1))
        mydb.commit()
        mydb.close()
        # function
        delete()
        messagebox.showinfo('Success', 'Saving is done :)')


def delete():
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

    # Delete this patient from schedule
    q = 'DELETE FROM nurse_sche WHERE day=%s AND time=%s'
    my_cursor.execute(q, (app_day.get(), app_date.get()))
    q = 'DELETE FROM pat_reserve WHERE day=%s AND time=%s'
    my_cursor.execute(q, (app_day.get(), app_date.get()))
    mydb.commit()
    mydb.close()


def connect_next():
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

    q = 'SELECT * FROM pat_reserve WHERE day=%s AND time=%s'
    my_cursor.execute(q, (app_day.get(), app_date.get()))
    row = my_cursor.fetchone()
    # Function
    insertion(row)
    mydb.commit()
    mydb.close()


# GUI design.
root = Tk()
root.title("DOCTOR")
root.resizable(False, False)

# Inserting an image
bg_im = ImageTk.PhotoImage(file="doctor.png")
bg_la = Label(root, image=bg_im)
bg_la.pack()

# Patient Name.
pat_label = Label(text='Patient Name', font=('Georgia', 12), bg="white", fg="#4D3FF8")
pat_label.place(x=130, y=120)
pat_entry = Entry(root, relief="flat", width=30, bg="#c3d7df", fg="purple", highlightthickness=1,
                  highlightbackground="orange", highlightcolor="blue")
pat_entry.place(x=130, y=150, height=22.5)

# Patient ID
phone_label = Label(text='Phone', font=('Georgia', 12), bg="white", fg="#4D3FF8")
phone_label.place(x=330, y=120)
phone_entry = Entry(root, relief="flat", width=29, bg="#c3d7df", fg="purple", highlightthickness=1,
                    highlightbackground="orange", highlightcolor="blue")
phone_entry.place(x=330, y=150, height=22.5)

# Pain
pain_label = Label(text='Patient Pain', font=('Georgia', 12), bg="white", fg="#4D3FF8")
pain_label.place(x=530, y=120)
pain_entry = Entry(root, relief="flat", width=40, bg="#c3d7df", fg="purple", highlightthickness=1,
                    highlightbackground="orange", highlightcolor="blue")
pain_entry.place(x=530, y=150, height=22.5)

# Test name
tst_label = Label(text='Test Name', font=('Georgia', 12), bg="white", fg="#4D3FF8")
tst_label.place(x=130, y=200)
tst_entry = Entry(root, relief="flat", width=40, bg="#c3d7df", fg="purple", highlightthickness=1,
                  highlightbackground="orange", highlightcolor="blue")
tst_entry.place(x=130, y=230, height=22.5)

# Diagnose name
dia_label = Label(text='Diagnose', font=('Georgia', 12), bg="white", fg="#4D3FF8")
dia_label.place(x=130, y=280)
dia_entry = Entry(root, relief="flat", width=40, bg="#c3d7df", fg="purple", highlightthickness=1,
                  highlightbackground="orange", highlightcolor="blue")
dia_entry.place(x=130, y=310, height=24)

# Prescription name
pre_label = Label(text='Prescription', font=('Georgia', 12), bg="white", fg="#4D3FF8")
pre_label.place(x=130, y=360)
pre_entry = Text(root, relief="flat", width=30, height=8, bg="#c3d7df", fg="purple", highlightthickness=1,
                 highlightbackground="orange", highlightcolor="blue")
pre_entry.place(x=130, y=390)

# The date
cal_label = Label(text='Date of Diagnose', font=('Georgia', 12), bg="white", fg="#4D3FF8")
cal_label.place(x=500, y=280)
cal_entry = DateEntry(root, width=30)
cal_entry.place(x=500, y=310)

# the save button
save_btn = Button(text="Save", width=14, font=("Georgia", 10, 'bold'), borderwidth=1,
                  background="blue", activebackground='orange', fg="white", cursor="hand2", command=connect_database)
save_btn.place(x=130, y=570)

# The clear button
cle_btn = Button(text="Clear", width=14, font=("Georgia", 10, 'bold'), borderwidth=1,
                 background="#BDB77A", activebackground='orange', fg="white", cursor="hand2", command=clear)
cle_btn.place(x=130, y=650)

# The next button
nex_btn = Button(text="Show Patient", width=20, font=("Georgia", 10, 'bold'), borderwidth=1,
                 background="#21D218", activebackground='orange', fg="white", cursor="hand2", command=connect_next)
nex_btn.place(x=875, y=610)

# This button direct you into a page has all examination info
pri_btn = Button(text="Print a report", width=14, font=("Georgia", 10, 'bold'), borderwidth=1,
                 background="brown", activebackground='orange', fg="white", cursor="hand2", command=imp_report)
pri_btn.place(x=900, y=650)

# The schedule of the button
sche_btn = Button(text="Schedule", width=9, font=("Arial", 9, 'bold'),
                  background="#fdd1a7", activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0, command=imp_sche)
sche_btn.place(x=3, y=208)

# The Log-out button
lout_btn = Button(text="Log out", width=9, font=("Arial", 9, 'bold'),
                  background="#fdd1a7", activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0, command=imp_log)
lout_btn.place(x=3, y=635)


l2 = Label(text="Day", bg="white", fg='#FC6130', font=("gray", 10))
l2.place(x=900, y=470)
app_day = Entry(root, relief="flat", width=20, bg="#D3F371", fg="purple", highlightthickness=1,
                highlightbackground="gray", highlightcolor="brown")
app_day.place(x=900, y=490, height=22.5)

l2 = Label(text="Time", bg="white", fg='#FC6130', font=("gray", 10))
l2.place(x=900, y=530)
app_date = Entry(root, relief="flat", width=20, bg="#D3F371", fg="purple", highlightthickness=1,
                 highlightbackground="gray", highlightcolor="brown")
app_date.place(x=900, y=550, height=22.5)

l2 = Label(text="Note: Go to Schedule page to know the reserved appointments.", bg="white", fg='gray', font=("Arial", 8))
l2.place(x=790, y=580)

root.mainloop()