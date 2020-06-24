# from tkinter import ttk
# import tkinter as tk
from tkinter import *
from tkinter.ttk import *


root = Tk()
root.title('Brute force')
root.iconbitmap('.icon')
root.geometry('800x600+300+100')
root.resizable(True, True)

style = Style()

style.configure('top.TFrame', background='red', relief='ridge', borderwidth=10)
top_frame = Frame(root, style='top.TFrame')
top_frame.pack(expand=True, fill='both', side='top')

style.configure('bot.TFrame', background='blue', relief='ridge', borderwidth=10)
bottom_frame = Frame(root, style='bot.TFrame')
bottom_frame.pack(expand=True, fill='both', side='bottom')

root.mainloop()
