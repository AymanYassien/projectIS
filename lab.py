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


def imp_nurse():
    window.destroy()
    import nurse


def imp_report():
    import lab_report


def disabled():
    Name_entry.config(state=DISABLED)


def clear():
    Patient_name_input.delete(0, END)
    Patient_phone_input.delete(0, END)
    Name_entry.delete(0, END)
    res_input.delete(0, END)
    Cost_input.delete(0, END)
    Date_input.delete(0, END)


# Database connection
def connect_search():
    if Patient_name_input.get() == '' or Patient_phone_input.get() == '':
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

        # Knowing the test name that doctor wrote it.
        q = 'SELECT * FROM dr_diagnose WHERE name=%s AND phone=%s'
        my_cursor.execute(q, (Patient_name_input.get(), Patient_phone_input.get()))
        row = my_cursor.fetchone()
        Name_entry.insert(0, row[4])
        disabled()
        mydb.commit()
        mydb.close()


def connect_save():
    if Patient_name_input.get() == '' or Patient_phone_input.get() == '' or res_input.get() == '' or Cost_input.get() == '' or Date_input.get() == '':
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

        # Updating Payment table
        q = 'UPDATE payment SET ana_cost=%s WHERE name=%s AND phone=%s'
        my_cursor.execute(q, (Cost_input.get(), Patient_name_input.get(), Patient_phone_input.get()))
        # Insert to LAB Table
        q = 'INSERT INTO lab_center(name, phone, test_name, result, cost, test_date, selected) VALUES(%s,%s,%s,%s,%s,%s,%s)'
        my_cursor.execute(q, (Patient_name_input.get(), Patient_phone_input.get(), Name_entry.get(),
                              res_input.get(), Cost_input.get(), Date_input.get(), 1))
        mydb.commit()
        mydb.close()
        messagebox.showinfo('Success :)', 'Save is Done')


window = Tk()
window.title("Lab")
window.resizable(False, False)  # no zoom in/out window

background_Image = ImageTk.PhotoImage(file="lab.png")
background_label = Label(window, image=background_Image)
background_label.pack()


Patient_name = Label(text='Patient Name', font=('Georgia', 12), background='white', fg='#8009F6')
Patient_name.place(x=130, y=120)
Patient_name_input = Entry(window, relief="flat", bg="#FAACDF", fg="green", highlightthickness=1,
                highlightbackground="gray", highlightcolor="blue",width=40)
Patient_name_input.place(x=130, y=150)

Patient_phone = Label(text='Patient Phone', font=('Georgia', 12), background='white', fg='#8009F6')
Patient_phone.place(x=500, y=120)
Patient_phone_input = Entry(window, relief="flat", bg="#FAACDF", fg="green", highlightthickness=1,
                highlightbackground="gray", highlightcolor="blue",width=40)
Patient_phone_input.place(x=500, y=150)

Name_label = Label(text='Name of Analysis', font=('Georgia', 12), background='white', fg='#8009F6')
Name_label.place(x=500, y=200)
Name_entry = Entry(window, relief="flat", bg="#FAACDF", fg="green", highlightthickness=1,
                highlightbackground="gray", highlightcolor="blue",width=40)
Name_entry.place(x=500, y=230)

Date_label = Label(text='Date of Analysis', font=('Georgia', 12), background='white', fg='#8009F6')
Date_label.place(x=130, y=300)
# Date_input = Entry(width=30)
Date_input = DateEntry(window, width=30)
Date_input.place(x=130, y=330)

res_label = Label(text='Result', font=('Georgia', 12), background='white', fg='#8009F6')
res_label.place(x=500, y=300)
res_input = Entry(window, relief="flat", bg="#FAACDF", fg="green", highlightthickness=1,
                highlightbackground="gray", highlightcolor="blue",width=30)
res_input.place(x=500, y=330)

Cost = Label(text='Analysis Cost', font=('Georgia', 12), background='white', fg='#8009F6')
Cost.place(x=500, y=380)
Cost_input = Entry(window, relief="flat", bg="#FAACDF", fg="green", highlightthickness=1,
                highlightbackground="gray", highlightcolor="blue",width=30)
Cost_input.place(x=500, y=410)

save_btn = Button(text="Save", width=11, cursor="hand2", font=("Georgia", 9, 'bold'), bg='#1D77FA',bd=1,fg='white', command=connect_save)
save_btn.place(x=530, y=500)

pri_btn = Button(text="Print a report", width=14, cursor="hand2", font=("Georgia", 9, 'bold'), bg='brown',bd=1,fg='white', command=imp_report)
pri_btn.place(x=900, y=525)

cancel_btn = Button(text="Clear", width=11, cursor="hand2", font=("Georgia", 9, 'bold'), bg='#F2E7F4',bd=1,fg='green', command=clear)
cancel_btn.place(x=530, y=550)

search_btn = Button(text="Search about name of test", width=25, font=("Georgia", 9, 'bold'), cursor="hand2",
                    bg='#AB2EF7',bd=1,fg='white', command=connect_search)
search_btn.place(x=150, y=230)


main_btn = Button(text="Main", width=9, font=("Arial", 9, 'bold'),
                  background="#fdd1a7", activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0, command=imp_nurse)
main_btn.place(x=3, y=340)

lout_btn = Button(text="Log out", width=9, font=("Arial", 9, 'bold'),
                  background="#fdd1a7", activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0, command=imp_log)
lout_btn.place(x=3, y=635)

window.mainloop()
