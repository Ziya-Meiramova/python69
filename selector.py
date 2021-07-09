from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry('500x500')
select1 = Combobox(window)
select1.grid(row='1', column='2')
select1['values'] = ("*", "2", "3", "4")
select1.current(2)
window.mainloop()
