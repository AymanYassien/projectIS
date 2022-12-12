# بسم الله الرحمن الرحيم

# Registration Page
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import mysql.connector


class Actions:
    def __init__(self, wind):
        self.root = wind

    def login_page(self):
        self.root.destroy()
        import login


def clear():
    user_entry.delete(0, END)
    email_entry.delete(0, END)
    pwd_entry.delete(0, END)
    con_entry.delete(0, END)
    check.set(0)


def connect_database():
    if user_entry.get() == '' or pwd_entry.get() == '' or con_entry.get() == '' or email_entry.get() == '':
        messagebox.showerror('ERROR :(', 'All Fields are Required.')
    elif pwd_entry.get() != con_entry.get():
        messagebox.showerror('ERROR :(', 'Password Mismatch.')
    elif check.get() == 0:
        messagebox.showerror('ERROR :(', 'Please Accept our Terms & Conditions.')
    else:  # Here, the connection.
        try:
            # The Connection method of MySQL
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Q,u5.S@2',
                port='3306',
                database='user_data'
            )
            # A pointer
            my_cursor = mydb.cursor()
        except:
            messagebox.showerror('ERROR', 'Database Connectivity Issue, Please Try Again.')
            return

        # Check if the user is already exist or not.
        query = 'SELECT * FROM data WHERE user_name=%s'
        my_cursor.execute(query, (user_entry.get(), ))
        # Now My cursor points at one row, so I will fetch it
        row = my_cursor.fetchone()
        # Checking
        if row != None:
            messagebox.showerror('ERROR :(', 'Username Already Exists, Try another username.')
            user_entry.delete(0, END)
        else:
            query = 'INSERT INTO data(user_name, email, password) VALUES(%s, %s, %s)'
            my_cursor.execute(query, (user_entry.get(), email_entry.get(), pwd_entry.get()))
            # committing the data that inserted into the database server.
            mydb.commit()
            # closing the connection of DB.
            mydb.close()
            messagebox.showinfo('Success', 'Registration Successful')
            # clear the data.
            clear()
            # Going to login page after signup.
            act.login_page()


# GUI design.
root = Tk()
root.title("SIGN UP")
root.resizable(False, False)

# A class that take actions.
act = Actions(root)

# Inserting an image
bgIm = ImageTk.PhotoImage(file="signup.png")
bgla = Label(root, image=bgIm)
bgla.pack()

# username label and entry box
user_label = Label(text="User Name", font=("courier", 12, "bold"), bg="white", fg="brown")
user_label.place(x=150, y=185)
user_entry = Entry(width=40, bg="#fdd1a7", fg="blue")
user_entry.place(x=150, y=210)

# email label and entry box
email_label = Label(text="Email", font=("courier", 12, "bold"), bg="white", fg="brown")
email_label.place(x=150, y=255)
email_entry = Entry(width=40, bg="#fdd1a7", fg="blue")
email_entry.place(x=150, y=280)

# password label and entry box
pwd_label = Label(text="Password", font=("courier", 12, "bold"), bg="white", fg="brown")
pwd_label.place(x=150, y=325)
pwd_entry = Entry(width=40, bg="#fdd1a7", fg="blue", show='*')
pwd_entry.place(x=150, y=350)

# confirm password label and entry box
con_label = Label(text="Confirm Password", font=("courier", 12, "bold"), bg="white", fg="brown")
con_label.place(x=150, y=395)
con_entry = Entry(width=40, bg="#fdd1a7", fg="blue", show='*')
con_entry.place(x=150, y=420)

# Condition check
check = IntVar()  # This variable will store either (1)if you press or (0)if not.
terms_check = Checkbutton(root, text="I agree to the Terms & Conditions", font=("Arial", 10, "bold"),
                          bg="white", fg="brown", cursor="hand2", variable=check)
terms_check.place(x=150, y=465)

# Sign up button
regis_btn = Button(text="Sign Up", width=14, font=("Arial", 12, "bold"), borderwidth=3, background="#ac6e52",
                   fg="white", cursor="hand2", command=connect_database)
regis_btn.place(x=200, y=510)

# Check if you have an account or not
already_label = Label(text="Already have an Account? ", font=("Arial", 10), bg="white", fg="orange")
already_label.place(x=150, y=570)

# Going to Login Page
login_btn = Button(text="Login", width=13, font=("Arial", 9, "bold underline"), bg="white", fg="blue",
                   cursor="hand2", bd=0, command=act.login_page)
login_btn.place(x=320, y=569)

root.mainloop()