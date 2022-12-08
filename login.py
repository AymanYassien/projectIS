from tkinter import *
from tkinter import ttk

window = Tk()
window.title("clinic management system")
window.geometry('1280x744+0+0')  # width - length - position
window.resizable(False, False)  # no zoom in/out window
window.configure(bg='#F0F0FF')

# ------------ Frame ------------

log_window = Frame(window, bg='white')
log_window.place(x=450, y=170, width=360, height=400)


window.mainloop()
