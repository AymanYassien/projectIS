# بسم الله الرحمن الرحيم

from tkinter import *
import mysql.connector
import pymysql
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry
from PIL import ImageTk


def imp_log():
    window.destroy()
    import login


def imp_lab():
    window.destroy()
    import lab


def clear():
    app_day.delete(0, END)
    app_date.delete(0, END)
    Total_Bill_input.delete(0, END)
    Remainder_input.delete(0, END)


def imp_sche():
    import nurse_sche


# Insertion of data in the patient profile
def insertion(row):
    Patient_name_input.insert(0, row[0])
    date.insert(0, row[1])
    Gender.insert(0, row[2])
    Patient_phone_input.insert(0, row[7])
    Payment_input.insert(0, 'Cash')
    disabled()


# After insertion, These fields become readonly.
def disabled():
    Patient_name_input.config(state=DISABLED)
    Patient_phone_input.config(state=DISABLED)
    Gender.config(state=DISABLED)
    date.config(state=DISABLED)
    Payment_input.config(state=DISABLED)


def connect_payment():
    if app_day.get() == '' or app_day.get() == '' or Payment_input.get() == '' or Remainder_input.get() == '':
        messagebox.showerror('ERROR :(', 'All Fields are Required.')
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

        q = 'INSERT INTO payment(name, phone, reserve_cost, ana_cost, debts) VALUES(%s,%s,%s,%s,%s)'
        my_cursor.execute(q, (Patient_name_input.get(), Patient_phone_input.get(), Total_Bill_input.get(), 0,Remainder_input.get()))
        mydb.commit()
        mydb.close()


def connect_accept():
    if app_day.get() == '' or app_day.get() == '' or Payment_input.get() == '' or Remainder_input.get() == '':
        messagebox.showerror('ERROR :(', 'All Fields are Required.')
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

        q = 'UPDATE nurse_sche SET status=%s WHERE day=%s AND time=%s'
        my_cursor.execute(q, ('Accepted', app_day.get(), app_date.get()))
        mydb.commit()
        mydb.close()
        messagebox.showinfo('Success :)', 'Successful Save')
        # Function
        connect_payment()


def connect_reject():
    if app_day.get() == '' or app_day.get() == '':
        messagebox.showerror('ERROR :(', 'All Fields are Required.')
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

        q = 'UPDATE nurse_sche SET status=%s WHERE day=%s AND time=%s'
        my_cursor.execute(q, ('Rejected', app_day.get(), app_date.get()))
        q = 'DELETE FROM pat_reserve WHERE day=%s AND time=%s'
        my_cursor.execute(q, (app_day.get(), app_date.get()))
        mydb.commit()
        mydb.close()
        messagebox.showinfo('Done :)', 'The Patient has been rejected :|')


def connect_search():
    if app_day.get() == '' or app_day.get() == '':
        messagebox.showerror('ERROR :(', 'All Fields are Required.')
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

        q = 'SELECT * FROM pat_reserve WHERE day=%s AND time=%s'
        my_cursor.execute(q, (app_day.get(), app_date.get()))
        row = my_cursor.fetchone()
        # Functions
        insertion(row)
        mydb.commit()
        mydb.close()


window = Tk()
window.title("NURSE")
window.resizable(False, False)  # no zoom in/out window

# Inserting an image
background_Image = ImageTk.PhotoImage(file="nurse.png")
background_label = Label(window, image=background_Image)
background_label.pack()

# ---------------------- Main buttons ----------------------
pro_btn = Button(text="Schedule", width=9, font=("Arial", 9, 'bold'), background="#fdd1a7",
                 activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0, command=imp_sche)
pro_btn.place(x=3, y=185)

# The schedule of the button
sche_btn = Button(text="LAB", width=9, font=("Arial", 9, 'bold'),
                  background="#fdd1a7", activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0, command=imp_lab)
sche_btn.place(x=3, y=405)

lout_btn = Button(text="Log out", width=9, font=("Arial", 9, 'bold'),
                  background="#fdd1a7", activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0, command=imp_log)
lout_btn.place(x=3, y=635)

# ---------------------- Main patient info ----------------------
Patient_name = Label(text='Patient Name ', font=('Georgia', 12), background='white', fg='#87CD22')
Patient_name.place(x=130, y=120)
Patient_name_input = Entry(window, relief="flat", bg="#FAA780", fg="purple", highlightthickness=1,
                highlightbackground="black", highlightcolor="blue",width=40)
Patient_name_input.place(x=130, y=150)

Patient_phone = Label(text='Patient Phone ', font=('Georgia', 12), background='white', fg='#87CD22')
Patient_phone.place(x=130, y=180)
Patient_phone_input = Entry(window, relief="flat", bg="#FAA780", fg="purple", highlightthickness=1,
                highlightbackground="black", highlightcolor="blue",width=40)
Patient_phone_input.place(x=130, y=210)

date = Label(text='DOB', font=('Georgia', 12), background='white', fg='#87CD22')
date.place(x=130, y=250)
date = Entry(window, relief="flat", bg="#FAA780", fg="purple", highlightthickness=1,
                highlightbackground="black", highlightcolor="blue",width=40)
date.place(x=130, y=280)

Gender = Label(text='Gender', font=('Georgia', 12), background='white', fg='#87CD22')
Gender.place(x=130, y=320)
Gender = Entry(window, relief="flat", bg="#FAA780", fg="purple", highlightthickness=1,
                highlightbackground="black", highlightcolor="blue",width=40)
Gender.place(x=130, y=350)

Payment = Label(text='Payment ', font=('Georgia', 12), background='white', fg='#87CD22')
Payment.place(x=130, y=390)
Payment_input = Entry(window, relief="flat", bg="#FAA780", fg="purple", highlightthickness=1,
                highlightbackground="black", highlightcolor="blue",width=40)
Payment_input.place(x=130, y=420)

Total_Bill = Label(text='Total Bill ', font=('Georgia', 12), background='white', fg='#87CD22')
Total_Bill.place(x=130, y=460)
Total_Bill_input = Entry(window, relief="flat", bg="#FAA780", fg="purple", highlightthickness=1,
                highlightbackground="black", highlightcolor="blue",width=40)
Total_Bill_input.place(x=130, y=490)

Remainder = Label(text='Debts', font=('Georgia', 12), background='white', fg='#87CD22')
Remainder.place(x=130, y=530)
Remainder_input = Entry(window, relief="flat", bg="#FAA780", fg="purple", highlightthickness=1,
                highlightbackground="black", highlightcolor="blue",width=40)
Remainder_input.place(x=130, y=560)


l2 = Label(text="Day", bg="white", fg='#87CD22', font=("gray", 11))
l2.place(x=500, y=120)
app_day = Entry(window, relief="flat", width=20, bg="#FAA780", fg="purple", highlightthickness=1,
                highlightbackground="black", highlightcolor="blue")
app_day.place(x=500, y=150, height=22.5)

l2 = Label(text="Time", bg="white", fg='#87CD22', font=("gray", 11))
l2.place(x=500, y=185)
app_date = Entry(window, relief="flat", width=20, bg="#FAA780", fg="purple", highlightthickness=1,
                 highlightbackground="black", highlightcolor="blue")
app_date.place(x=500, y=210, height=22.5)


search_btn = Button(text="Search", width=12, font=("Georgia", 9, 'bold'), cursor="hand2",
                    bg='#CE62F9',bd=1,fg='white', command=connect_search)
search_btn.place(x=700, y=175)

Accept_btn = Button(text="Accept", width=12, font=("Georgia", 9, 'bold'), cursor="hand2", bg='#2766F7',bd=1,fg='white', command=connect_accept)
Accept_btn.place(x=500, y=380)

re_btn = Button(text="Reject", width=12, font=("Georgia", 9, 'bold'), cursor="hand2", bg='#EE5141',bd=1, fg='white', command=connect_reject)
re_btn.place(x=500, y=430)

cancel_btn = Button(text="Clear", width=12, font=("Georgia", 9, 'bold'), cursor="hand2", bg='#E0F8BD',bd=1, fg='green', command=clear)
cancel_btn.place(x=500, y=480)

# Disable fields
# disabled()

window.mainloop()