import sys, time, os
from tkinter import *
from tkinter import ttk

title = "Air Quality Assessor 3000"
author = "Mitchell Charity"

root = Tk()
root.title(title)

frame = ttk.Frame(root, padding = "3 3 12 12")
frame.grid(column = 0, row = 0, sticky = (N, S, E, W))
frame.columnconfigure(0, weight = 1)
frame.rowconfigure(0, weight = 1)

ozone = StringVar()

o_entry = ttk.Entry(frame, width = 7, testvariable = ozone)
o_entry.grid(column = 2, row = 1, sticky = (W, E))


root.mainloop()