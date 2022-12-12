from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
# import pyttsx3
from tkcalendar import Calendar,DateEntry
from PIL import ImageTk

# init ****************************************
window = Tk()
window.title("Patient")
window.resizable(False, False)

# photo *********************************************
img = ImageTk.PhotoImage(file="ma.png")
label = Label(window, image=img)
label.pack()



# name*********************************
def click(event):
    pt1.config(state=NORMAL)
    pt1.delete(0, END)


pt1 = Entry(window, bg="#c78767", fg="black", relief="flat", font=("family", 10), highlightthickness=1,
            highlightbackground="#f5b03b", highlightcolor="#c78767"
            , selectbackground="#fdd1a7", selectforeground="#f5b03b")
pt1.insert(0, "Enter Your Name")
pt1.config(state=DISABLED)
pt1.bind("<Button>", click)
pt1.place(x=120, y=110, width=200, height=25)

l2 = Label(text=" Patient Name", highlightcolor="#f5b03b",bg="white",foreground="black",highlightbackground="#fdd1a7",font=("gray",10))
l2.place(x=100 ,y=90,width= 120 ,height=20)




# phone ***********************************
def click(event):
    pt2.config(state=NORMAL)
    pt2.delete(0, END)


pt2 = Entry(window, bg="#c78767", fg="black", relief="flat", font=("family", 10), highlightthickness=1,
            highlightbackground="#f5b03b", highlightcolor="#c78767"
            , selectbackground="#fdd1a7", selectforeground="#f5b03b")
pt2.insert(0, "Enter Your Phone")
pt2.config(state=DISABLED)
pt2.bind("<Button>", click)
pt2.place(x=120, y=200, width=200, height=25)


l2 = Label(text=" Patient Phone", highlightcolor="#f5b03b",bg="white",foreground="black",highlightbackground="black",font=("black",10))
l2.place(x=100 ,y=180,width= 120 ,height=20)




# gander ***********************************************
gender_combobox = Combobox(window, values=['Male', 'Female'], font="brown 10", state='r',
background="green",foreground="black")
gender_combobox.place(x=120, y=405, width=200, height=25)


l2 = Label(text=" Patient Gander", highlightcolor="#f5b03b",bg="white",foreground="black",highlightbackground="black",font=("black",10))
l2.place(x=100 ,y=385,width= 120 ,height=20)




# adress ***********************************************
def click(event):
    pt4.config(state=NORMAL)
    pt4.delete(0, END)

pt4 = Entry(window, bg="#c78767", fg="black", relief="flat", font=("family", 10), highlightthickness=1,
            highlightbackground="#f5b03b", highlightcolor="#c78767"
            , selectbackground="#fdd1a7", selectforeground="#f5b03b")
pt4.insert(0, "Enter Your Adress")
pt4.config(state=DISABLED)
pt4.bind("<Button>", click)
pt4.place(x=120, y=290, width=200, height=50)


l2 = Label(text=" Patient Adress", highlightcolor="#f5b03b",bg="white",foreground="black",highlightbackground="black",font=("black",10))
l2.place(x=100 ,y=270,width= 120 ,height=20)


# DATE

l2 = Label(text="Date of Birth", highlightcolor="#f5b03b",bg="white",foreground="black",highlightbackground="black",font=("black",10) )
l2.place(x=100 ,y=480,width= 120 ,height=20)


cal = DateEntry(window,selectmode='day', highlightcolor="#f5b03b",bg="white",foreground="black",highlightbackground="black",font=("black",10),height=15)
cal.place(x=120,y=500,width= 200,height=25)

gender_combobox = Combobox(window, values=['Doc.1', 'Doc','Doc3'], font="brown 10", state='r',
background="green",foreground="black")
gender_combobox.place(x=120, y=590, width=200, height=25)


l2 = Label(text="Choose doc", highlightcolor="#f5b03b",bg="white",foreground="black",highlightbackground="black",font=("black",10))
l2.place(x=100 ,y=570,width= 120 ,height=20)


#* edit ***************
f1=Button(window,text="Edit",highlightcolor="#f5b03b",bg="yellow",foreground="black",highlightbackground="black",font=("black",12),height=8)
f1.place(x=430,y =210,width=150,height=25)
#* save ***************
f1=Button(window,text="Save",highlightcolor="#f5b03b",bg="brown",foreground="yellow",highlightbackground="black",font=("black",12),height=8)
f1.place(x=430,y =250,width=150,height=25)

#* save ***************
f1=Button(window,text="Clear",highlightcolor="#f5b03b",bg="gray",foreground="black",highlightbackground="black",font=("black",12),height=8)
f1.place(x=430,y =290,width=150,height=25)


#**show
f1=Button(window,text="Show Doctor Profile",highlightcolor="#f5b03b",bg="gray",foreground="black",highlightbackground="black",font=("black",12),height=8,width=15)
f1.place(x=430,y =330,width=150,height=25)


window.mainloop()
