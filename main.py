import tkinter as tk
from tkinter import *
from turtle import width

### colors
color1 = '#A5F2C0'
color2 = '#DE9EE8'
color3 = '#DBB99F'
color4 = '#B0BCF5'
color5 = '#E0E89E'
white = '#ffffff'


window = tk.Tk()
window.geometry('300x400')
window.title('Calculadora')
window.resizable(False, False)
window.config(bg=color1)


line = Label(window, text='', width=30, height=3, relief='flat', anchor='center',bg=white)
line.place(x=28,y=20)

### linha da esquerda
botao_c = Button(window, text='c', width=2, height=1)
botao_c.place(x=50, y=100)

botao_7 = Button(window, text='7', width=2, height=1)
botao_7.place(x=50, y=150)

botao_4 = Button(window, text='4', width=2, height=1)
botao_4.place(x=50, y=200)

botao_1 = Button(window, text='1', width=2, height=1)
botao_1.place(x=50, y=250)

botao_0 = Button(window, text='0', width=2, height=1)
botao_0.place(x=50, y=300)

### linha do meio
botao_del = Button(window, text='del', width=2, height=1)
botao_del.place(x=100, y=100)

botao_8 = Button(window, text='8', width=2, height=1)
botao_8.place(x=100, y=150)

botao_5 = Button(window, text='5', width=2, height=1)
botao_5.place(x=100, y=200)

botao_2 = Button(window, text='2', width=2, height=1)
botao_2.place(x=100, y=250)

botao_virg = Button(window, text=',', width=2, height=1)
botao_virg.place(x=100, y=300)

###linha da direita
botao_porc = Button(window, text='%', width=2, height=1)
botao_porc.place(x=150, y=100)

botao_9 = Button(window, text='9', width=2, height=1)
botao_9.place(x=150, y=150)

botao_6 = Button(window, text='6', width=2, height=1)
botao_6.place(x=150, y=200)

botao_3 = Button(window, text='3', width=2, height=1)
botao_3.place(x=150, y=250)

botao_igual = Button(window, text='=', width=8, height=1)
botao_igual.place(x=150, y=300)


### linha dos operadores
botao_div = Button(window, text='÷', width=2, height=1)
botao_div.place(x=200, y=100)

botao_mult = Button(window, text='x', width=2, height=1)
botao_mult.place(x=200, y=150)

botao_sub = Button(window, text='-', width=2, height=1)
botao_sub.place(x=200, y=200)

botao_adc = Button(window, text='+', width=2, height=1)
botao_adc.place(x=200, y=250)



window.mainloop()