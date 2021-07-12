
from math import *
from tkinter import *

window = Tk()
window.geometry('700x500')
window.resizable(width=False, height=False)
window.title("Quadratic  calculator")

frame = Frame(window)
frame.grid()

a = Entry(frame, width=3)
a.grid(row=1, column=1, padx= 0)

a_txt = Label(frame, text='x**2 + ')
a_txt.grid(row=1, column=2)

b = Entry(frame, width = 3)
b.grid(row=1, column = 3)

b_txt = Label(frame, text = 'x + ')
b_txt.grid(row = 1, column = 4)

c = Entry(frame, width= 3)
c.grid(row=1, column= 5)


output = Label(frame, bg = "lightblue", font="Arial 10", width=80, height=10)
output.grid(row=3, columnspan=8)

def comb(a):
    output.configure(text=a)

def solver(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + sqrt(D)) / 2*a
        x2 = (-b - sqrt(D)) / 2*a
        text = "Discriminant is {}. x1 is equal to {}. x2 is equal to {}"
        s = text.format(D, x1, x2)
    else:
        s = "No solution"
    return s


def inp1():
    a_value = float(a.get())
    b_value = float(b.get())
    c_value = float(c.get())
    comb(solver(a_value, b_value, c_value))

btn = Button(frame, text='Solve', command=inp1).grid(row=1, column=7)

window.mainloop()