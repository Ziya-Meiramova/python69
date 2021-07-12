# game
from tkinter import *
from random import *
def f1():
    global cnt
    c = 1
    cnt = cnt - c
    if cnt <= 0:
        pal.configure(text="Вы проиграли!!!!", fg="red")
    else:
        pal.configure(text= cnt*"  I")
def f2():
    global cnt
    c = 2
    cnt = cnt - c
    if cnt <= 0:
        pal.configure(text="Вы проиграли!!!!", fg="red")
    else:
        pal.configure(text= cnt*"  I")
def f3():
    global cnt
    c = 3
    cnt = cnt - c
    if cnt <= 0:
        pal.configure(text="Вы проиграли!!!!", fg="red")
    else:
        pal.configure(text=cnt * "  I")
def pc():
    global cnt
    c = randint(1, 3)
    if cnt == 4:
        c = 3
    elif cnt == 3:
        c = 2
    elif cnt == 2:
        c = 1
    cnt = cnt - c
    if cnt <= 0:
        pal.configure(text='Вы выиграли!!!', fg="green")
    else:
        pal.configure(text=cnt * "  I")

cnt = 20
window = Tk()
window.geometry('700x500')
window.resizable(0, 0)
window.title("Palo4ki")

text1 = Label(window, text='Сколько палочек вам нужно?')
text1.config(font=("Arial", 20, "bold"))
text1.grid(row=0, column=10)

btn1 = Button(window, text="1", command=f1)
btn1.grid(row=1, column=2, columnspan = 2)

btn2 = Button(window, text="2",command=f2)
btn2.grid(row=1, column= 10, columnspan=2)

btn3 = Button(window, text="3", command=f3)
btn3.grid(row = 1, column=20, columnspan=2)

pal = Label(window, text=cnt*"  I", fg = "green")
pal.config(font = ("Arial", 30, "bold"))
pal.grid(row = 2, column=10)

btn_pc = Button(window, text='Ход компьютера', width=30, command=pc)
btn_pc.grid(row = 3, column= 10)

window.mainloop()