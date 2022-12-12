# بسم الله الرحمن الرحيم

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import mysql.connector


def clear():
    user_entry.delete(0, END)
    pwd_entry.delete(0, END)


def connect_database():
    if user_entry.get() == '' or pwd_entry.get() == '':
        messagebox.showerror('ERROR :(', 'All Fields are Required.')
    else:
        try:
            con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Q,u5.S@2',
                port='3306',
                database='user_data'
            )
            mycursor = con.cursor()
        except:
            messagebox.showerror('ERROR', 'Connection is not established try again')
            return

        query = 'select * from data where user_name=%s and password=%s'
        mycursor.execute(query, (user_entry.get(), pwd_entry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('ERROR :(', 'Invalid username or password')
            user_entry.delete(0, END)
            pwd_entry.delete(0, END)
        elif user_entry.get() == 'doctor1' and pwd_entry.get() == '000':
            messagebox.showinfo('WELCOME :)', 'Successful Login')
            con.close()
            clear()
            root.destroy()
            import doctor
        else:
            messagebox.showinfo('WELCOME :)', 'Successful Login')
            con.close()
            clear()
            root.destroy()
            import patient


def signup_page():
    root.destroy()
    import signup


# GUI design.
root = Tk()
root.title("LOGIN")
root.resizable(False, False)  # no zoom in/out window

# Inserting an image
bgIm = ImageTk.PhotoImage(file="Login.png")
bgla = Label(root, image=bgIm)
bgla.pack()  # ?

# username label and entry box
user_label =Label(text="User Name", font=("courier", 12, "bold"), bg="white", fg="brown")
user_label.place(x=430, y=169)
user_entry =Entry(width=40, bg="#fdd1a7", fg="blue")
user_entry.place(x=430, y=195)

# password label and entry box
pwd_label = Label(text="Password", font=("courier", 12, "bold"), bg="white", fg="brown")
pwd_label.place(x=430, y=240)
pwd_entry = Entry(width=40, bg="#fdd1a7", fg="blue")
pwd_entry.config(show="*")
pwd_entry.place(x=430, y=266)


# Login button
login_btn = Button(text="Login", width=11, font=("Arial", 12, "bold"),
                  borderwidth=3, background="#ac6e52", fg="white", cursor="hand2", command=connect_database)
login_btn.place(x=483, y=310)

# Check if you forget password
already_label = Label(text="Create a new account?", font=("Arial", 10), bg="white", fg="orange")
already_label.place(x=430, y=370)

# Going to Login Page
sign_btn = Button(text="SignUp", width=13, font=("Arial", 9, "bold underline"), bg="white",
                      fg="blue", cursor="hand2", bd=0, command=signup_page)
sign_btn.place(x=565, y=370)

root.mainloop()
