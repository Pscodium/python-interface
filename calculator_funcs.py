import tkinter as tk

### colors
color1 = '#A5F2C0'
color2 = '#DE9EE8'
color3 = '#DBB99F'
color4 = '#B0BCF5'
color5 = '#E0E89E'
white = '#ffffff'



def make_window() -> tk.Tk:
    window = tk.Tk()
    window.title('Calculadora')
    window.geometry('300x400')
    window.title('Calculadora')
    window.resizable(False, False)
    window.config(bg=color1)
    
    return window