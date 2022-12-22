# بسم الله الرحمن الرحيم

# Registration Page
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter import ttk
import pymysql
import mysql.connector


def is_valid_username(username):
    if len(username) <= 3 or len(username) >= 20:
        return False
    else:
        num = True
        for char in username:
            if char.isdigit():
                num = False
        return num


def is_valid_email(email):
    if len(email) <= 10 or len(email) > 30:
        return False
    if email[-1] == '.':
        return False
    if email[-2] == '.':
        return False
    if email[-3] == '.':
        return False
    else:
        check_at = False
        at = '@'
        check_dot = False
        dot = '.'
        space = True

        for char in email:
            if char.isspace():
                space = False
                break
            if char == at:
                check_at = True
            if char == dot:
                check_dot = True

        return space and check_at and check_dot


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
    elif not is_valid_username(user_entry.get()):
        messagebox.showerror('ERROR :(', 'Username must taller than 3 & less than 20 & No number')
    elif not is_valid_email(email_entry.get()):
        messagebox.showerror('ERROR :(', 'Email invalid')
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
            query = 'INSERT INTO data(user_name, email, password, have_profile) VALUES(%s, %s, %s, %s)'
            my_cursor.execute(query, (user_entry.get(), email_entry.get(), pwd_entry.get(), ''))
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
user_label = Label(text="User Name", font=("courier", 12, "bold"), bg="white", fg="#ba5135")
user_label.place(x=150, y=185)
user_entry = Entry(root, relief="flat", width=40, bg="#fdd1a7", fg="purple", highlightthickness=1,
                   highlightbackground="brown", highlightcolor="red")
user_entry.place(x=150, y=210)

# email label and entry box
email_label = Label(text="Email", font=("courier", 12, "bold"), bg="white", fg="#ba5135")
email_label.place(x=150, y=255)
email_entry = Entry(root, relief="flat", width=40, bg="#fdd1a7", fg="purple", highlightthickness=1,
                    highlightbackground="brown", highlightcolor="red")
email_entry.place(x=150, y=280)

# password label and entry box
pwd_label = Label(text="Password", font=("courier", 12, "bold"), bg="white", fg="#ba5135")
pwd_label.place(x=150, y=325)
pwd_entry = Entry(root, relief="flat", width=40, bg="#fdd1a7", fg="purple", highlightthickness=1,
                  highlightbackground="brown", highlightcolor="red", show='*')
pwd_entry.place(x=150, y=350)

# confirm password label and entry box
con_label = Label(text="Confirm Password", font=("courier", 12, "bold"), bg="white", fg="#ba5135")
con_label.place(x=150, y=395)
con_entry = Entry(root, relief="flat", width=40, bg="#fdd1a7", fg="purple", highlightthickness=1,
                  highlightbackground="brown", highlightcolor="red", show='*')
con_entry.place(x=150, y=420)

# Condition check
check = IntVar()  # This variable will store either (1)if you press or (0)if not.
terms_check = Checkbutton(root, text="I agree to the Terms & Conditions", font=("Arial", 10, "bold"),
                          bg="white", fg="#ba5135", cursor="hand2", variable=check)
terms_check.place(x=150, y=465)

# Sign up button
regis_btn = Button(text="Sign Up", width=14, font=("Arial", 12, "bold"), borderwidth=1, background="#ac6e52",
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