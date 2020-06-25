import tkinter.ttk as ttk
import tkinter as tk
# from tkinter import *
# from tkinter.ttk import *


root = tk.Tk()
root.title('Brute force')
root.iconbitmap('.icon')
root.geometry('800x600+300+100')
root.resizable(True, True)

style = ttk.Style()

style.configure('top.TFrame', background='red', relief='ridge', borderwidth=10)
top_frame = ttk.Frame(root, style='top.TFrame')
top_frame.pack(expand=False, fill='both', side='top')

style.configure('bot.TFrame', background='blue', relief='ridge', borderwidth=10)
bottom_frame = ttk.Frame(root, style='bot.TFrame')
bottom_frame.pack(expand=False, fill='both', side='bottom')

# output_screen = tk.Text(bottom_frame, height=20, width=96, bg='#2b2b2b', fg='#668156', font='Menlo 14', wrap='word')
output_screen = tk.Text(bottom_frame, height=20, width=96, bg='#000000', fg='#64c864', font='Menlo 14', wrap='word')
# output_screen = tk.Text(bottom_frame, font='Menlo 14', wrap='word')
# output_screen.grid(row=0, column=0, rowspan=7, columnspan=9, sticky='nesw')
output_screen.pack(expand=False, fill=None)

root.mainloop()
