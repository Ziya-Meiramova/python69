from tkinter import *

window = Tk()
window.title("Calculator")
window.minsize(350, 375)
window.resizable(False, False)
input_text = StringVar()

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set(expression)

def btn_equal():
    global expression # "3 + 7"
    result = str(eval(expression))
    input_text.set(result)
    expression = " "
expression = ""

input_frame = Frame(window, width = 350, height = 50, bg ="blue", bd = 5)
input_frame.pack(side=TOP )

input_entry = Entry(input_frame, font=('arial', 20, 'bold'), width = 30, bg = "blue", justify = RIGHT, textvariable=input_text)
input_entry.grid(row=0, column=0)
input_entry.pack(pady = 10)

btn_frame = Frame(window, width=350, height = 280, bg = "grey")
btn_frame.pack()

ac_btn = Button(btn_frame, text="AC", fg = "black", bg="white", width = 14, height = 3, cursor="hand1", command = lambda: btn_clear()).grid(row=0, column = 0, columnspan = 2, pady = 1, padx = 1)
divide_btn = Button(btn_frame, text="/", fg="black", bg = "white", width = 14, height = 3, cursor = "hand1", command = lambda: btn_click("/")).grid(row = 0, column = 2, columnspan = 2, padx = 1, pady = 1)

seven = Button(btn_frame, text="7", fg = "black", bg = "white", width = 5, height = 3, cursor = "hand1", command=lambda: btn_click("7")).grid(row = 1, column = 0, padx = 1, pady=1)
eight = Button(btn_frame, text="8", fg = "black", bg = "white", width = 5, height = 3, cursor = "hand1", command=lambda: btn_click("8")).grid(row = 1, column = 1, padx = 1, pady=1)
nine = Button(btn_frame, text="9", fg = "black", bg = "white", width = 5, height = 3, cursor = "hand1", command=lambda: btn_click("9")).grid(row = 1, column = 2, padx = 1, pady=1)
multi = Button(btn_frame, text="*", fg = "black", bg = "white", width = 5, height = 3, cursor = "hand1", command=lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady=1)

four = Button(btn_frame, text="4", fg = "black", bg = "white", width = 5, height = 3, cursor = "hand1", command=lambda: btn_click("4")).grid(row = 2, column = 0, padx = 1, pady=1)
five = Button(btn_frame, text="5", fg = "black", bg = "white", width = 5, height = 3, cursor = "hand1", command=lambda: btn_click("5")).grid(row = 2, column = 1, padx = 1, pady=1)
six = Button(btn_frame, text="6", fg = "black", bg = "white", width = 5, height = 3, cursor = "hand1", command=lambda: btn_click("6")).grid(row = 2, column = 2, padx = 1, pady=1)
minus = Button(btn_frame, text="-", fg = "black", bg = "white", width = 5, height = 3, cursor = "hand1", command=lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady=1)

one = Button(btn_frame, text="1", fg = "black", bg = "white", width = 5, height = 3, cursor = "hand1", command=lambda: btn_click("1")).grid(row = 3, column = 0, padx = 1, pady=1)
two = Button(btn_frame, text="2", fg = "black", bg = "white", width = 5, height = 3, cursor = "hand1", command=lambda: btn_click("2")).grid(row = 3, column = 1, padx = 1, pady=1)
three = Button(btn_frame, text="3", fg = "black", bg = "white", width = 5, height = 3, cursor = "hand1", command=lambda: btn_click("3")).grid(row = 3, column = 2, padx = 1, pady=1)
plus = Button(btn_frame, text="+", fg = "black", bg = "white", width = 5, height = 3, cursor = "hand1", command=lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady=1)

zero = Button(btn_frame, text="0", fg = "black", bg="white", width = 14, height = 3, cursor="hand1", command = lambda: btn_click("0")).grid(row=4, column = 0, columnspan = 2, pady = 1, padx = 1)
dot = Button(btn_frame, text=".", fg = "black", bg = "white", width = 5, height = 3, cursor = "hand1", command=lambda: btn_click("+")).grid(row = 4, column = 2, padx = 1, pady=1)
equall = Button(btn_frame, text="=", fg = "black", bg = "white", width = 5, height = 3, cursor = "hand1", command=lambda: btn_equal()).grid(row = 4, column = 3, padx = 1, pady=1)







window.mainloop()