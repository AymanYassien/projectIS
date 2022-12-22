# بسم الله الرحمن الرحيم

from tkinter import *
import mysql.connector
import pymysql
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from PIL import ImageTk


def imp_login():
    root.destroy()
    import login


def is_valid_password(password):
    if 8 <= len(password) <= 20:
        upper = False
        lower = False
        num = False
        space = True

        for char in password:
            if char.isdigit():
                num = True
            if char.islower():
                lower = True
            if char.isupper():
                upper = True
            if char.isspace():
                space = False

        return num and lower and upper and space
    else:
        return False


def connect_database():
    if user_entry.get() == '' or pwd_entry.get() == '' or con_entry.get() == '':
        messagebox.showerror('ERROR :(', 'All Fields are Required.')
    elif pwd_entry.get() != con_entry.get():
        messagebox.showerror('ERROR :(', 'Password Mismatch.')
    elif not is_valid_password(pwd_entry.get()):
        messagebox.showerror('ERROR :(', 'Password must be has Capital & small & Number & No Space')
    else:  # Here, the connection.
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

        query = 'UPDATE data SET password=%s WHERE user_name=%s'
        my_cursor.execute(query, (pwd_entry.get(), user_entry.get()))
        query = 'UPDATE patient_profile SET password=%s WHERE name=%s'
        my_cursor.execute(query, (pwd_entry.get(), user_entry.get()))
        # committing the data that inserted into the database server.
        mydb.commit()
        # closing the connection of DB.
        mydb.close()
        messagebox.showinfo('Success', 'You have just insert new password, Go to login page :)')


# GUI design.
root = Tk()
root.title("RESET PASSWORD")
root.resizable(False, False)

# Inserting an image
bg_im = ImageTk.PhotoImage(file="reset.png")
bg_la = Label(root, image=bg_im)
bg_la.pack()


# username label and entry box
user_label = Label(text="User Name", font=("courier", 12, "bold"), bg="white", fg="#ba5135")
user_label.place(x=150, y=185)
user_entry = Entry(root, relief="flat", width=40, bg="#fdd1a7", fg="purple", highlightthickness=1,
                   highlightbackground="brown", highlightcolor="red")
user_entry.place(x=150, y=210)

# password label and entry box
pwd_label = Label(text="Password", font=("courier", 12, "bold"), bg="white", fg="#ba5135")
pwd_label.place(x=150, y=280)
pwd_entry = Entry(root, relief="flat", width=40, bg="#fdd1a7", fg="purple", highlightthickness=1,
                  highlightbackground="brown", highlightcolor="red", show='*')
pwd_entry.place(x=150, y=305)

# confirm password label and entry box
con_label = Label(text="Confirm Password", font=("courier", 12, "bold"), bg="white", fg="#ba5135")
con_label.place(x=150, y=375)
con_entry = Entry(root, relief="flat", width=40, bg="#fdd1a7", fg="purple", highlightthickness=1,
                  highlightbackground="brown", highlightcolor="red", show='*')
con_entry.place(x=150, y=400)

# Condition check
regis_btn = Button(text="Save", width=12, font=("Arial", 10, "bold"), borderwidth=1, background="#B667E7",
                   fg="white", cursor="hand2", command=connect_database)
regis_btn.place(x=220, y=480)

log_btn = Button(text="Go To Login Page", width=18, font=("Arial", 10, "bold"), borderwidth=1, background="#EAA812",
                   fg="white", cursor="hand2", command=imp_login)
log_btn.place(x=200, y=530)

root.mainloop()