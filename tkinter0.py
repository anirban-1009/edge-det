#tkinter0.py
from tkinter import *

def print_val(val):
    print(val)
master = Tk()
w = Scale(master, from_=100, to=200, command=print_val)
w.pack()
print(w)
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()

mainloop()