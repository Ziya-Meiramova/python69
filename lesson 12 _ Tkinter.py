from tkinter import *
from tkinter.ttk import *
root = Tk()
root.geometry('500x500')

# def print_name():
#     txt = input1.get()
#     print(txt)

# def print_name2():
#     txt = input1.get()
#     lbl1.configure(text=txt, bg='#8c12b8', width='12')
#     lbl2.configure(text=txt, bg = txt)

def print_name3():
    a = input1.get()
    b = input2.get()
    lbl1.configure(bg=a, fg = b)



lbl1 = Label(root, text='Hello', bg='red', fg='white', width='10', height='2')
# lbl1.pack()
lbl1.grid(row='0', column='0')
lbl2 = Label(root, text='Hello', bg='blue', width='10', height='2' )
lbl2.grid(row='1', column='1')

input1 = Entry(root, bg='yellow')
input1.grid(row='0', column='1')
input2 = Entry(root)
input2.grid(row='0', column='2')

btn1 = Button(root, text='Click', bg='#7fba7f', command = print_name3)
btn1.grid(row='1', column='0')

select1 = Combobox(root)
select1.grid(row='5', column='5')
select1['values'] = ("1", '2', '3', '4')
root.mainloop()
