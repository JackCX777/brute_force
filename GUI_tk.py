# from tkinter import ttk
# import tkinter as tk
from tkinter import *
from tkinter.ttk import *


root = Tk()
root.geometry('800x600')

style = Style()

style.configure('top.TFrame', background='red', relief='ridge')
top_frame = Frame(root, style='top.TFrame')
# top_frame.pack(expand=True, fill='both', side='top')
top_frame.pack(expand=True, fill='both')

style.configure('bot.TFrame', background='blue', relief='ridge')
bottom_frame = Frame(root, style='bot.TFrame')
# bottom_frame.pack(expand=True, fill='both', side='bottom')
bottom_frame.pack(expand=True, fill='both')

root.mainloop()
