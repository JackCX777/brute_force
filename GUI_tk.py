# from tkinter import ttk
# import tkinter as tk
from tkinter import *
from tkinter.ttk import *


root = Tk()
root.geometry('800x600')

style = Style()

style.configure('top.TFrame', background='red', relief='ridge', padding=6, width=100, height=100)
top_frame = Frame(root, width=100, height=100, style='top.TFrame')
top_frame.pack(fill='both', expand=True, anchor='s')

style.configure('bot.TFrame', background='blue', relief='ridge', padding=6, width=100, height=100)
bottom_frame = Frame(root, style='bot.TFrame')
bottom_frame.pack(expand=True, fill=BOTH, side='bottom', anchor='s')


root.mainloop()
