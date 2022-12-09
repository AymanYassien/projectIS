# بسم الله الرحمن الرحيم

# Registration Page
import tkinter as tk
from PIL import ImageTk


# This Func will be completed when the login page be finished
# I will import the login file here to link with signup page.
def login_page():
    root.destroy()
    import login


# GUI design.
root = tk.Tk()
root.title("SIGN UP")
# root.geometry("680x500")
# root.configure(background="#88F9D2")

# Inserting an image
bgIm = ImageTk.PhotoImage(file="signup.png")
bgla = tk.Label(root, image=bgIm)
bgla.pack()

# username label and entry box
user_label = tk.Label(text="User Name", font=("courier", 12, "bold"), bg="white", fg="brown")
user_label.place(x=150, y=185)
user_entry = tk.Entry(width=40, bg="#fdd1a7", fg="blue")
user_entry.place(x=150, y=210)

# email label and entry box
email_label = tk.Label(text="Email", font=("courier", 12, "bold"), bg="white", fg="brown")
email_label.place(x=150, y=255)
email_entry = tk.Entry(width=40, bg="#fdd1a7", fg="blue")
email_entry.place(x=150, y=280)

# password label and entry box
pwd_label = tk.Label(text="Password", font=("courier", 12, "bold"), bg="white", fg="brown")
pwd_label.place(x=150, y=325)
pwd_entry = tk.Entry(width=40, bg="#fdd1a7", fg="blue")
pwd_entry.place(x=150, y=350)

# confirm password label and entry box
con_label = tk.Label(text="Confirm Password", font=("courier", 12, "bold"), bg="white", fg="brown")
con_label.place(x=150, y=395)
con_entry = tk.Entry(width=40, bg="#fdd1a7", fg="blue")
con_entry.place(x=150, y=420)

# Condition check
terms_check = tk.Checkbutton(root, text="I agree to the Terms & Conditions",
                             font=("Arial", 10, "bold"), bg="white", fg="brown")
terms_check.place(x=150, y=465)

# Sign up button
regis_btn = tk.Button(text="Sign Up", width=14, font=("Arial", 12, "bold"),
                      borderwidth=3, background="#ac6e52", fg="white")
regis_btn.place(x=200, y=510)

# Check if you have an account or not
already_label = tk.Label(text="Already have an Account? ", font=("Arial", 10), bg="white", fg="orange")
already_label.place(x=150, y=570)

# Going to Login Page
login_btn = tk.Button(text="Login", width=13, font=("Arial", 9, "bold underline"), bg="white",
                      fg="blue", cursor="hand2", bd=0, command=login_page)
login_btn.place(x=320, y=569)

root.mainloop()