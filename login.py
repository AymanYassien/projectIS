from tkinter import *
# from tkinter import ttk

window = Tk()
window.title("clinic management system")
window.geometry('1280x744+0+0')  # width - length - position
window.resizable(False, False)  # no zoom in/out window
window.configure(bg='#F0F0FF')

# ------------ Frame ------------

log_window = Frame(window, bg='#FFFFFA')
log_window.place(x=450, y=170, width=360, height=270)

log_window_title = Label(log_window, text='Login', font=('Calibri', 24, 'bold'), background='white', fg='#7F7FFF')
log_window_title.place(x=149, y=1)

user_name = Label(log_window, text='User Name :', font=('Calibri', 16), background='white', fg='#7F7FFF')
user_name.place(x=1, y=80)
user_name_input = Entry(log_window, width=20, font=('Calibri', 16))
user_name_input.place(x=1, y=105)

Password = Label(log_window, text='Password :', font=('Calibri', 16), background='white', fg='#7F7FFF')
Password.place(x=1, y=145)
Password_input = Entry(log_window, width=20, font=('Calibri', 16))
Password_input.place(x=1, y=175)


Forget_Password = Label(log_window, text='Forget Password ?', font=('Calibri', 12, 'underline'),
                        background='white', fg='red')
Forget_Password.place(x=1, y=220)

Register = Label(log_window, text='Create a new account', font=('Calibri', 12), background='white', fg='#7F7FFF')
Register.place(x=1, y=240)


window.mainloop()
