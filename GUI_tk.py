# from tkinter import ttk
# import tkinter as tk
from tkinter import *
from tkinter.ttk import *


root = Tk()
root.geometry('800x600')

style = Style()
style.configure('br.TFrame', foreground='red', background='black')
style.map('br.TFrame',
          highlightcolor=[('focus', 'green'),
                        ('!focus', 'red')])

frame = Frame(root, style='br.TFrame')
frame.pack(expand=True, fill=BOTH)
bottomframe = Frame(root, style='br.TFrame')
bottomframe.pack(expand=True, fill=BOTH, side='bottom')

root.mainloop()
