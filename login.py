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
                database='doctor_table'
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
        elif user_entry.get() == 'doctor' and pwd_entry.get() == '000':
            messagebox.showinfo('WELCOME :)', 'Successful Login')
            con.close()
            clear()
            root.destroy()
            import doctor
        elif user_entry.get() == 'nurse' and pwd_entry.get() == '001':
            messagebox.showinfo('WELCOME :)', 'Successful Login')
            con.close()
            clear()
            root.destroy()
            import nurse
        else:
            messagebox.showinfo('WELCOME :)', 'Successful Login')
            con.close()
            clear()
            root.destroy()
            import patient


def signup_page():
    root.destroy()
    import signup


def reset_page():
    root.destroy()
    import reset_pass


# GUI design.
root = Tk()
root.title("LOGIN")
root.resizable(False, False)  # no zoom in/out window

# Inserting an image
bgIm = ImageTk.PhotoImage(file="Login.png")
bgla = Label(root, image=bgIm)
bgla.pack()  # ?

# username label and entry box
user_label = Label(text="User Name", font=("courier", 12, "bold"), bg="white", fg="#ba5135")
user_label.place(x=430, y=180)
user_entry = Entry(root, relief="flat", width=40, bg="#fdd1a7", fg="purple", highlightthickness=1,
                   highlightbackground="brown", highlightcolor="red")
user_entry.place(x=430, y=210)

# password label and entry box
pwd_label = Label(text="Password", font=("courier", 12, "bold"), bg="white", fg="#ba5135")
pwd_label.place(x=430, y=270)
pwd_entry = Entry(root, relief="flat", width=40, bg="#fdd1a7", fg="purple", highlightthickness=1,
                  highlightbackground="brown", highlightcolor="red")
pwd_entry.config(show="*")
pwd_entry.place(x=430, y=300)


# Login button
login_btn = Button(text="Login", width=14, font=("Arial", 11, "bold"),
                   borderwidth=1, background="#ac6e52", fg="white", cursor="hand2", command=connect_database)
login_btn.place(x=483, y=380)

# Check if you forget password
already_label = Label(text="Create a new account?", font=("Arial", 10), bg="white", fg="orange")
already_label.place(x=430, y=470)

# Going to Login Page
sign_btn = Button(text="SignUp", width=13, font=("Arial", 9, "bold underline"), bg="white",
                      fg="blue", cursor="hand2", bd=0, command=signup_page)
sign_btn.place(x=565, y=470)


# Check if you forget password
already_label = Label(text="Forget Password?", font=("Arial", 10), bg="white", fg="orange")
already_label.place(x=430, y=520)

# Going to Login Page
sign_btn = Button(text="Reset Password", width=13, font=("Arial", 9, "bold underline"), bg="white",
                      fg="blue", cursor="hand2", bd=0, command=reset_page)
sign_btn.place(x=565, y=520)

root.mainloop()
