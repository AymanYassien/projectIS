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


def imp_sche():
    import pat_sche


def imp_pat_pri():
    import pat_report


def imp_profile():
    window.destroy()
    import dr_profile


# Insertion of data in the patient profile
def insertion(row):
    name.insert(0, row[1])
    phone.insert(0, row[2])
    gender.insert(0, row[3])
    bod.insert(0, row[4])
    adress.insert(0, row[6])
    state.insert(0, row[7])


# After insertion, These fields become readonly.
def disabled():
    name.config(state=DISABLED)
    phone.config(state=DISABLED)
    gender.config(state=DISABLED)
    bod.config(state=DISABLED)
    adress.config(state=DISABLED)
    state.config(state=DISABLED)


# as soon as the page appears
def connect_database():
    try:
        mydb = mysql.connector.Connect(
            host='localhost',
            user='root',
            password='Q,u5.S@2',
            port='3306',
            database='doctor_table'
        )
        my_cursor = mydb.cursor()
    except:
        messagebox.showerror("Error", "Database Connectivity Issue,Please Try Again")
        return

    query = 'SELECT * FROM patient_profile WHERE selected=%s'
    my_cursor.execute(query, (1, ))
    row = my_cursor.fetchone()
    # Functions
    insertion(row)
    q = 'UPDATE patient_profile SET selected=%s WHERE phone=%s'
    my_cursor.execute(q, (0, phone.get()))
    disabled()
    mydb.commit()
    mydb.close()


# save button
def connect_db():
    if pain.get(0.0, END) == '' or app_day.get() == '' or app_day.get() == '':
        messagebox.showerror('ERROR :(', 'All Fields are Required.')
    else:
        try:
            mydb = mysql.connector.Connect(
                host='localhost',
                user='root',
                password='Q,u5.S@2',
                port='3306',
                database='doctor_table'
            )
        except:
            messagebox.showerror("Error", "Database Connectivity Issue,Please Try Again")
            return

        my_cursor = mydb.cursor()
        q = 'INSERT INTO pat_reserve(name, bod, gender, pain, day, time, phone) VALUES(%s,%s,%s,%s,%s,%s,%s)'
        my_cursor.execute(q, (name.get(), bod.get(), gender.get(), pain.get(0.0, END), app_day.get(), app_date.get(), phone.get()))
        messagebox.showinfo('Success :)', 'The Process is Completely Successfully')
        q = 'INSERT INTO nurse_sche(day, time, status) VALUES(%s,%s,%s)'
        my_cursor.execute(q, (app_day.get(), app_date.get(), 'Pending'))
        # delete the record of timetable after selecting an appointment.
        q = 'DELETE FROM time_sche WHERE day=%s AND time=%s'
        my_cursor.execute(q, (app_day.get(), app_date.get()))
        # make a field to connect the report treeview with these data (pat_report)
        q = 'UPDATE pat_reserve SET selected=%s WHERE name=%s'
        my_cursor.execute(q, (1, name.get()))
        mydb.commit()
        mydb.close()


# GUI design.
window = Tk()
window.title("PATIENT PROFILE")
window.resizable(False, False)

# Inserting an image
bg_im = ImageTk.PhotoImage(file="patpro.png")
bg_la = Label(window, image=bg_im)
bg_la.pack()

# name
name = Entry(window, relief="flat", width=40, bg="#D3F371", fg="purple", highlightthickness=1,
             highlightbackground="gray", highlightcolor="brown")
name.place(x=130, y=230, height=22.5)

l2 = Label(text="Patient Name", bg="white", fg='#FC6130', font=("gray", 12))
l2.place(x=130, y=200)

# phone
phone = Entry(window, relief="flat", width=40, bg="#D3F371", fg="purple", highlightthickness=1,
              highlightbackground="gray", highlightcolor="brown")
phone.place(x=130, y=310, height=22.5)

l2 = Label(text="Patient Phone", bg="white", fg='#FC6130', font=("gray", 12))
l2.place(x=130, y=280)

# gender
gender = Entry(window, relief="flat", width=40, bg="#D3F371", fg="purple", highlightthickness=1,
               highlightbackground="gray", highlightcolor="brown")
gender.place(x=130, y=630, height=22.5)
l2 = Label(text="Patient Gender", bg="white", fg='#FC6130', font=("gray", 12))
l2.place(x=130, y=600)

# adress
adress = Entry(window, relief="flat", width=40, bg="#D3F371", fg="purple", highlightthickness=1,
               highlightbackground="gray", highlightcolor="brown")
adress.place(x=130, y=390, height=22.5)
l2 = Label(text="Patient Adress", bg="white", fg='#FC6130', font=("gray", 12))
l2.place(x=130, y=360)

# State
state = Entry(window, relief="flat", width=40, bg="#D3F371", fg="purple", highlightthickness=1,
              highlightbackground="gray", highlightcolor="brown")
state.place(x=130, y=470, height=22.5)

l2 = Label(text="State", bg="white", fg='#FC6130', font=("gray", 12))
l2.place(x=130, y=440)

# BOD
bod = Entry(window, relief="flat", width=40, bg="#D3F371", fg="purple", highlightthickness=1,
            highlightbackground="gray", highlightcolor="brown")
bod.place(x=130, y=550, height=22.5)
l2 = Label(text="Birth Date", bg="white", fg='#FC6130', font=("gray", 12))
l2.place(x=130, y=520)

# Pain
pain = Text(window, relief="flat", width=30, bg="#D3F371", fg="purple", highlightthickness=1,
            highlightbackground="gray", highlightcolor="brown", height=4)
pain.place(x=500, y=310)
l2 = Label(text="Describe Your Pain", bg="white", fg='#FC6130', font=("gray", 12))
l2.place(x=500, y=280)

# Appointment
l2 = Label(text="Choose an Appointment", bg="white", fg='#FC6130', font=("gray", 12))
l2.place(x=500, y=440)

l2 = Label(text="Day", bg="white", fg='#FC6130', font=("gray", 10))
l2.place(x=500, y=470)
app_day = Entry(window, relief="flat", width=20, bg="#D3F371", fg="purple", highlightthickness=1,
                highlightbackground="gray", highlightcolor="brown")
app_day.place(x=500, y=490, height=22.5)

l2 = Label(text="Time", bg="white", fg='#FC6130', font=("gray", 10))
l2.place(x=640, y=470)
app_date = Entry(window, relief="flat", width=20, bg="#D3F371", fg="purple", highlightthickness=1,
                 highlightbackground="gray", highlightcolor="brown")
app_date.place(x=640, y=490, height=22.5)

l2 = Label(text="Note: Go to Schedule page to know the valid appointments.", bg="white", fg='gray', font=("Arial", 8))
l2.place(x=500, y=520)


pro_btn = Button(text="Dr Profile", width=9, font=("Arial", 9, 'bold'), background="#fdd1a7",
                 activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0, command=imp_profile)
pro_btn.place(x=3, y=208)

# The schedule of the button
sche_btn = Button(text="Schedule", width=9, font=("Arial", 9, 'bold'),
                  background="#fdd1a7", activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0, command=imp_sche)
sche_btn.place(x=3, y=405)

lout_btn = Button(text="Log out", width=9, font=("Arial", 9, 'bold'),
                  background="#fdd1a7", activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0, command=imp_log)
lout_btn.place(x=3, y=635)

# the save button
save_btn = Button(text="Save", width=14, font=("Georgia", 10, 'bold'), borderwidth=1,
                  background="blue", activebackground='orange', fg="white", cursor="hand2", command=connect_db)
save_btn.place(x=900, y=580)

# This button direct you into a page has all examination info
pri_btn = Button(text="Print a report", width=14, font=("Georgia", 10, 'bold'), borderwidth=1,
                 background="brown", activebackground='orange', fg="white", cursor="hand2", command=imp_pat_pri)
pri_btn.place(x=900, y=630)


# Linking the patient data with his profile
connect_database()


window.mainloop()