"""
#1 UI
#2 wörter reinkriegen / libary -> csv + json


# google translate api
"""

from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('800x600')

frm = ttk.Frame(window, padding=10)
frm.grid()

ttk.Label(frm, text="Hello!").grid(column=1, row=0)
ttk.Label(frm, text="Hallo!").grid(column=2, row=0)
ttk.Button(frm, text="Quit", command=window.destroy).grid(column=5, row=0)

e = Entry(frm).grid(row=0, column=6)

window.mainloop()
