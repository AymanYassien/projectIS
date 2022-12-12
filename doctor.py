# بسم الله الرحمن الرحيم

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry
# import pymysql
# import mysql.connector


root = Tk()
root.title("DOCTOR")
root.resizable(False, False)

# Inserting an image
bg_im = ImageTk.PhotoImage(file="doctor.png")
bg_la = Label(root, image=bg_im)
bg_la.pack()


pat_label = Label(text='Patient Name', font=('Georgia', 12), bg="white", fg="#4D3FF8")
pat_label.place(x=130, y=120)
pat_entry = Entry(width=40, bg="#fdd1a7", fg="green")
pat_entry.insert(0, 'Ahmed')
pat_entry.config(state='disabled')
pat_entry.place(x=130, y=150)

id_label = Label(text='Patient ID', font=('Georgia', 12), bg="white", fg="#4D3FF8")
id_label.place(x=500, y=120)
id_entry = Entry(width=30, bg="#fdd1a7", fg="green")
id_entry.insert(0, '1')
id_entry.config(state='disabled')
id_entry.place(x=500, y=150)

tst_label = Label(text='Test Name', font=('Georgia', 12), bg="white", fg="#4D3FF8")
tst_label.place(x=130, y=200)
tst_entry = Entry(width=40, bg="#fdd1a7", fg="green")
tst_entry.place(x=130, y=230)

dia_label = Label(text='Diagnose', font=('Georgia', 12), bg="white", fg="#4D3FF8")
dia_label.place(x=130, y=280)
dia_entry = Entry(width=40, bg="#fdd1a7", fg="green")
dia_entry.place(x=130, y=310)

pre_label = Label(text='Prescription', font=('Georgia', 12), bg="white", fg="#4D3FF8")
pre_label.place(x=130, y=360)
pre_entry = Text(width=30, height=6, bg="#fdd1a7", fg="green")
pre_entry.place(x=130, y=390)

# add_label = Label(text='Additional Costs', font=('Georgia', 12), bg="white", fg="#4D3FF8")
# add_label.place(x=130, y=520)
# add_entry = Entry(width=40, bg="#fdd1a7", fg="green")
# add_entry.place(x=130, y=550)

cal_label = Label(text='Date of Diagnose', font=('Georgia', 12), bg="white", fg="#4D3FF8")
cal_label.place(x=500, y=280)
cal_entry = DateEntry(root, width=30)
cal_entry.place(x=500, y=310)


his_btn = Button(text="Show Medical History", width=19, font=("Georgia", 10, 'bold'), borderwidth=2,
                 background="#6256F7", fg="white", cursor="hand2")
his_btn.place(x=500, y=200)

save_btn = Button(text="Save", width=14, font=("Georgia", 10, 'bold'), borderwidth=2,
                  background="#6256F7", fg="white", cursor="hand2")
save_btn.place(x=130, y=570)

cle_btn = Button(text="Clear", width=14, font=("Georgia", 10, 'bold'), borderwidth=2,
                 background="#BDB77A", fg="white", cursor="hand2")
cle_btn.place(x=130, y=650)

nex_btn = Button(text="Next", width=14, font=("Georgia", 10, 'bold'), borderwidth=2,
                 background="#70E121", fg="white", cursor="hand2")
nex_btn.place(x=900, y=570)

pri_btn = Button(text="Print a report", width=14, font=("Georgia", 10, 'bold'), borderwidth=2,
                 background="brown", fg="white", cursor="hand2")
pri_btn.place(x=900, y=650)

root.mainloop()