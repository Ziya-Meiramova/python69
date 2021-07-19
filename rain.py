from tkinter import *

window = Tk()
window.title("Color")
window.minsize(700,400)
window.resizable(False, False)

def clicked(color):
    window['bg'] = color
    lbl.config(text=color)


btn_1 = Button(window, text="Каждый", padx = 20, pady = 8, font='14')
btn_1.grid(row=0, column=0)
btn_1.config(command=lambda: clicked("red"))

btn_2 = Button(window, text="Охотник", padx = 20, pady = 8, font='14')
btn_2.grid(row=1, column=1)
btn_2.config(command=lambda: clicked("orange"))

btn_3 = Button(window, text="Желает", padx = 20, pady = 8, font='14')
btn_3.grid(row=2, column=2)
btn_3.config(command=lambda: clicked("yellow"))

btn_4 = Button(window, text="Знать", padx = 20, pady = 8, font='14')
btn_4.grid(row=3, column=3)
btn_4.config(command=lambda: clicked("green"))

btn_5 = Button(window, text="Где", padx = 20, pady = 8, font='14')
btn_5.grid(row=4, column=4)
btn_5.config(command=lambda: clicked("#40eaed"))

btn_6 = Button(window, text="Сидит", padx = 20, pady = 8, font='14')
btn_6.grid(row=5, column=5)
btn_6.config(command=lambda: clicked("blue"))

btn_7 = Button(window, text="Фазан", padx = 20, pady = 8, font='14')
btn_7.grid(row=6, column=6)
btn_7.config(command=lambda: clicked("purple"))

lbl = Label(window, font=('Arial', 20, 'bold'), width=15, height = 1, bg = "white", text="Hello")
lbl.grid(column=0, row = 5)
window.mainloop()