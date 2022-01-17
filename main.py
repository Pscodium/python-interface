import tkinter as tk
from tkinter import *

### colors
color1 = '#A5F2C0'
color2 = '#DE9EE8'
color3 = '#DBB99F'
color4 = '#B0BCF5'
color5 = '#E0E89E'


window = tk.Tk()
window.geometry('300x300')
window.title('Python Project')
window.resizable(False, False)
window.config(bg=color1)


up_frame = Frame(window, width=300, height=50, bg=color4, relief='flat')
up_frame.grid(row=0, column=0, sticky=NSEW)

down_frame = Frame(window, width=300, height=250, bg=color1, relief='flat')
down_frame.grid(row=1, column=0, sticky=NSEW)


window.mainloop()