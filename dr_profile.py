# بس الله الرحمن الرحيم

from tkinter import *
from PIL import ImageTk


def imp_log():
    root.destroy()
    import login


def imp_main_data():
    root.destroy()
    import patient


def imp_main_pro():
    root.destroy()
    import pat_profile


# GUI design.
root = Tk()
root.title("DOCTOR PROFILE")
root.resizable(False, False)

# Inserting an image
bg_im = ImageTk.PhotoImage(file="drprofile.png")
bg_la = Label(root, image=bg_im)
bg_la.pack()

# Doctor name
dr_label = Label(text='Doctor Name', font=('Georgia', 12), bg="white", fg="#3d5a80")
dr_label.place(x=130, y=235)
dr_entry = Entry(root, relief="flat", width=35, bg="#c3d7df", fg="purple", highlightthickness=1,
                 highlightbackground="orange", highlightcolor="blue")
dr_entry.insert(0, "Mark Hall")
dr_entry.config(state=DISABLED)
dr_entry.place(x=130, y=260, height=22.5)

# Doctor phone.
ph_label = Label(text='Doctor Phone', font=('Georgia', 12), bg="white", fg="#3d5a80")
ph_label.place(x=130, y=300)
ph_entry = Entry(root, relief="flat", width=35, bg="#c3d7df", fg="purple", highlightthickness=1,
                 highlightbackground="orange", highlightcolor="blue")
ph_entry.insert(0, "(111) 121-2121")
ph_entry.config(state=DISABLED)
ph_entry.place(x=130, y=325, height=22.5)

# Doctor Email.
em_label = Label(text='Doctor Email', font=('Georgia', 12), bg="white", fg="#3d5a80")
em_label.place(x=130, y=365)
em_entry = Entry(root, relief="flat", width=35, bg="#c3d7df", fg="purple", highlightthickness=1,
                 highlightbackground="orange", highlightcolor="blue")
em_entry.insert(0, "markhall@email.com")
em_entry.config(state=DISABLED)
em_entry.place(x=130, y=390, height=22.5)

# Doctor Gender.
gen_label = Label(text='Gender', font=('Georgia', 12), bg="white", fg="#3d5a80")
gen_label.place(x=130, y=430)
gen_entry = Entry(root, relief="flat", width=35, bg="#c3d7df", fg="purple", highlightthickness=1,
                  highlightbackground="orange", highlightcolor="blue")
gen_entry.insert(0, "Male")
gen_entry.config(state=DISABLED)
gen_entry.place(x=130, y=455)

# Specialist of a doctor.
sp_label = Label(text='Specialist in', font=('Georgia', 12), bg="white", fg="#3d5a80")
sp_label.place(x=130, y=495)
sp_entry = Entry(root, relief="flat", width=35, bg="#c3d7df", fg="purple", highlightthickness=1,
                 highlightbackground="orange", highlightcolor="blue")
sp_entry.insert(0, "Infectious diseases")
sp_entry.config(state=DISABLED)
sp_entry.place(x=130, y=520, height=22.5)

# Graduation
grad_label = Label(text='Graduated From', font=('Georgia', 12), bg="white", fg="#3d5a80")
grad_label.place(x=130, y=560)
grad_entry = Entry(root, relief="flat", width=35, bg="#c3d7df", fg="purple", highlightthickness=1,
                   highlightbackground="orange", highlightcolor="blue")
grad_entry.insert(0, "University Of California, Mars 2007")
grad_entry.config(state=DISABLED)
grad_entry.place(x=130, y=585, height=22.5)

# DOB
cal_label = Label(text='Date of Birth', font=('Georgia', 12), bg="white", fg="#3d5a80")
cal_label.place(x=480, y=235)
cal_entry = Entry(root, relief="flat", width=35, bg="#c3d7df", fg="purple", highlightthickness=1,
                  highlightbackground="orange", highlightcolor="blue")
cal_entry.insert(0, "27-02-1972")
cal_entry.config(state=DISABLED)
cal_entry.place(x=480, y=260)

# Address of Clinic
add_label = Label(text='Clinic Address', font=('Georgia', 12), bg="white", fg="#3d5a80")
add_label.place(x=480, y=300)
add_entry = Text(root, relief="flat", width=30, height=5, bg="#F2F2F2", font=('Arial', 9), fg="gray", highlightthickness=1,
                 highlightbackground="orange", highlightcolor="blue")
add_entry.insert(0.0, "3031 Brannon Street, Los Angeles, CA 90017")
add_entry.config(state=DISABLED)
add_entry.place(x=480, y=325)

# Social Media.
soc_label = Label(text='Social Media', font=('Georgia', 12), bg="white", fg="#3d5a80")
soc_label.place(x=480, y=430)

# Directing to patient page.
main_btn = Button(text="Main data", width=9, font=("Arial", 9, 'bold'),
                  background="#fdd1a7", activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0, command=imp_main_data)
main_btn.place(x=3, y=230)
main_btn = Button(text="Main profile", width=9, font=("Arial", 9, 'bold'),
                  background="#fdd1a7", activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0, command=imp_main_pro)
main_btn.place(x=3, y=315)

# Logging out.
lout_btn = Button(text="Log out", width=9, font=("Arial", 9, 'bold'),
                  background="#fdd1a7", activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0, command=imp_log)
lout_btn.place(x=3, y=635)

root.mainloop()