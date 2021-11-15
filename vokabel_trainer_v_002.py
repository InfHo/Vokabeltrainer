"""
#1 UI
#2 wörter reinkriegen / libary -> csv + json


# google translate api
"""

from tkinter import *
from tkinter import ttk
from dict_woerterbuch import words 
import random 

window = Tk()
window.geometry('800x600')

frm = ttk.Frame(window, padding=10)
frm.grid()


def display_new_exercise():
    global y
    y = random.choice(list(words.keys()))
    anzeige.configure(text=str(y))
    print(y, ">>>>", words[y])


#ttk.Label(frm, text="Hello!").grid(column=1, row=0)
anzeige = ttk.Label(frm, text="Hallo!")
anzeige.grid(column=2, row=0)
ttk.Button(frm, text="Quit", command=window.destroy).grid(column=5, row=0)
#ttk.Label(frm, text=words).grid(column=3, row=0)
ttk.Button(frm, text="Neue Aufgabe", command=display_new_exercise).grid(column=4, row=0)

e = Entry(frm)
e.grid(row=0, column=6)

def testfunktion():
    print(e.get())
    print("^^^",words[y],y)
    if e.get() == words[y]:
        print("richtig")
    else:
        print("falsch")

ttk.Button(frm, text="test", command=testfunktion).grid(column=0,row=0)

window.mainloop()
