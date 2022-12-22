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


def imp_profile():
    window.destroy()
    import dr_profile


def link():
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
    q = 'UPDATE patient_profile SET selected=%s WHERE password=%s'
    my_cursor.execute(q, (1, pwd.get()))
    mydb.commit()
    mydb.close()


def imp_mypro():
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
    q = 'SELECT * FROM data WHERE password=%s'
    my_cursor.execute(q, (pwd.get(), ))
    row = my_cursor.fetchone()
    if row == None or row[1] == 'doctor' or row[1] == 'nurse':
        messagebox.showerror('ERROR :(', 'Wrong Password ;)')
    elif row[4] == '':
        messagebox.showerror('Warning :|', 'You are new here :) Please, Enter your data first.')
    else:
        mydb.commit()
        mydb.close()
        # function
        link()
        window.destroy()
        import pat_profile


def connect():
    try:
        mydb2 = mysql.connector.Connect(
            host='localhost',
            user='root',
            password='Q,u5.S@2',
            port='3306',
            database='doctor_table'
        )
    except:
        messagebox.showerror("Error", "Database Connectivity Issue,Please Try Again")
        return

    my_cursor2 = mydb2.cursor()
    q = 'UPDATE data SET have_profile=%s WHERE password=%s'
    my_cursor2.execute(q, ('y', pwd.get()))
    mydb2.commit()
    mydb2.close()


# connect to data base
def connect_database():
    if name.get() == '' or phone.get() == '' or adress.get() == '' or gender_combobox.get() == '' or birth.get() == '' or state.get() == '':
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
            my_cursor = mydb.cursor()
        except:
            messagebox.showerror("Error", "Database Connectivity Issue,Please Try Again")
            return

        query = 'insert into patient_profile(name, phone, gender, birth_date, address, state, selected, password)values(%s,%s,%s,%s,%s,%s, %s, %s)'
        my_cursor.execute(query, (name.get(), phone.get(), gender_combobox.get(), birth.get(), adress.get(), state.get(), 0, pwd.get()))
        mydb.commit()
        mydb.close()
        messagebox.showinfo('Success :)', 'The Process is Completely Successfully, Go TO Your Profile')
        # Function
        connect()


def clear():
    name.delete(0, END)
    phone.delete(0, END)
    adress.delete(0, END)
    gender_combobox.delete(0, END)
    birth.delete(0, END)


# init ************GUI****************************
window = Tk()
window.title("PATIENT")
window.resizable(False, False)

# photo
img = ImageTk.PhotoImage(file="patient.png")
label = Label(window, image=img)
label.pack()

# name
name = Entry(window, relief="flat", width=40, bg="#D3F371", fg="purple", highlightthickness=1,
             highlightbackground="gray", highlightcolor="brown")
name.place(x=130, y=160, height=22.5)

l2 = Label(text="Patient Name", bg="white", fg='#FC6130', font=("gray", 12))
l2.place(x=130, y=130)

# phone
phone = Entry(window, relief="flat", width=40, bg="#D3F371", fg="purple", highlightthickness=1,
              highlightbackground="gray", highlightcolor="brown")
phone.place(x=130, y=240, height=22.5)

l2 = Label(text="Patient Phone", bg="white", fg='#FC6130', font=("gray", 12))
l2.place(x=130, y=210)

# gender
gender_combobox = Combobox(window, values=['Male', 'Female'], width=32, font="brown 10", state='r')
gender_combobox.place(x=130, y=480, height=22.5)
l2 = Label(text="Patient Gender", bg="white", fg='#FC6130', font=("gray", 12))
l2.place(x=130, y=450)

# adress
adress = Entry(window, relief="flat", width=40, bg="#D3F371", fg="purple", highlightthickness=1,
               highlightbackground="gray", highlightcolor="brown")
adress.place(x=130, y=320, height=22.5)
l2 = Label(text="Patient Address", bg="white", fg='#FC6130', font=("gray", 12))
l2.place(x=130, y=290)

# State
state = Entry(window, relief="flat", width=40, bg="#D3F371", fg="purple", highlightthickness=1,
              highlightbackground="gray", highlightcolor="brown")
state.place(x=130, y=400, height=22.5)
l2 = Label(text="State", bg="white", fg='#FC6130', font=("gray", 12))
l2.place(x=130, y=370)

# DATE
l2 = Label(text="Date of Birth", bg="white", fg='#FC6130', font=("gray", 12))
l2.place(x=450, y=130)
birth = DateEntry(window, selectmode='day', width=32, highlightcolor="#f5b03b",bg="white",
                  foreground="black",highlightbackground="black",font=("black",10),height=15)
birth.place(x=450, y=160, width=200, height=22.5)

# Show patient profile
pwd = Entry(window, relief="flat", width=24, bg="#D3F371", fg="purple", highlightthickness=1,
            highlightbackground="gray", highlightcolor="brown", show='*')
pwd.place(x=900, y=530, height=22.5)
l2 = Label(text="Enter your password", bg="white", fg='#FC6130', font=("gray", 12))
l2.place(x=900, y=500)
f1 = Button(window,text="Show My Profile",highlightcolor="#f5b03b",bg="#FC6130",foreground="white",
            highlightbackground="black", cursor='hand2', font=("black",12),height=8, command=imp_mypro)
f1.place(x=900,y =600,width=150,height=25)

# save
f1=Button(window,text="Save", highlightcolor="#f5b03b", bg="blue", foreground="white",
          highlightbackground="black", font=("black", 12), cursor='hand2', height=8, command=connect_database)
f1.place(x=130,y =570,width=150,height=25)

# clear
f1=Button(window,text="Clear",highlightcolor="#f5b03b",bg="gray",foreground="white",
          highlightbackground="black",font=("black",12), cursor='hand2', height=8,command=clear)
f1.place(x=130,y =630,width=150,height=25)

pro_btn = Button(text="Dr Profile", width=9, font=("Arial", 9, 'bold'), background="#fdd1a7",
                 activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0, command=imp_profile)
pro_btn.place(x=3, y=208)

lout_btn = Button(text="Log out", width=9, font=("Arial", 9, 'bold'),
                  background="#fdd1a7", activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0, command=imp_log)
lout_btn.place(x=3, y=635)

window.mainloop()