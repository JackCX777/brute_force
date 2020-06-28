import tkinter.ttk as ttk
import tkinter as tk
# from PIL import ImageTk, Image

# This code will replace tkinter widgets by ttk widgets
# from tkinter import *
# from tkinter.ttk import *


root = tk.Tk()
root.title('Brute force')
# For windows only?
# root.iconbitmap('python.ico')
# Using TCL:
# icon_img = tk.PhotoImage(file='./Users/jack/PycharmProjects/Brute_force/safe-breaking.gif')
# root.tk.call('wm', 'iconphoto', root._w, icon_img)
# Here False for insert icon_img only to root window:
# root.iconphoto(False, tk.PhotoImage(file='./Users/jack/PycharmProjects/Brute_force/safe-breaking.gif'))
# root.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(Image.open('./Users/jack/PycharmProjects/Brute_force/safe-breaking.gif')))
root.geometry('800x600+300+100')
root.resizable(True, True)

root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='safe-breaking.png'))

# style = ttk.Style()
#
# # style.configure('top.TFrame', background='red', relief='ridge', borderwidth=10)
# style.configure('top.TFrame', background='red', foreground='red', relief='ridge', borderwidth=10)
# top_frame = ttk.Frame(root, style='top.TFrame')
# # top_frame.pack(expand=True, fill='x', side='top', anchor='center')
# top_frame.pack(expand=True, fill='x')
#
# # style.configure('bot.TFrame', background='blue', relief='ridge', borderwidth=10)
# style.configure('bot.TFrame', background='blue', foreground='blue',  relief='ridge', borderwidth=10)
# bottom_frame = ttk.Frame(root, style='bot.TFrame')
# # bottom_frame.pack(expand=True, fill='x', side='bottom', anchor='center')
# bottom_frame.pack(expand=True, fill='x')
#
# # output_screen = tk.Text(bottom_frame, height=20, width=96, bg='#2b2b2b', fg='#668156', font='Menlo 14', wrap='word')
# # output_screen = tk.Text(bottom_frame, height=20, width=96, bg='#000000', fg='#64c864', font='Menlo 14', wrap='word')
# # output_screen = tk.Text(bottom_frame, font='Menlo 14', wrap='word')
# # output_screen.grid(row=0, column=0, rowspan=7, columnspan=9, sticky='nesw')
# # output_screen.pack(expand=False, fill=None)


# Anchor option working only with expand option
#
# Using tk:
#
# top_frame = tk.Frame(root, background='red', relief='ridge', borderwidth=5, height=100)
# top_frame.pack(expand=False, fill='x', side='top', anchor='n')
#
# center_frame = tk.Frame(root, background='green', relief='ridge', borderwidth=5, height=100)
# center_frame.pack(expand=True, fill='x', anchor='center', padx=5)
#
# bottom_frame = tk.Frame(root, background='blue', relief='ridge', borderwidth=5, height=400)
# bottom_frame.pack(expand=False, fill='x', side='bottom', anchor='s', padx=5, pady=5)

# Using ttk:
#
style = ttk.Style()

style.configure('top.TFrame', background='red', foreground='red', relief='ridge', borderwidth=5, height=100)
top_frame = ttk.Frame(root, style='top.TFrame')
top_frame.pack(expand=False, fill='x', side='top', anchor='n')

style.configure('center.TFrame', background='green', foreground='green', relief='ridge', borderwidth=5, height=100)
center_frame = ttk.Frame(root, style='center.TFrame')
center_frame.pack(expand=True, fill='x', anchor='center', padx=5)

style.configure('bottom.TFrame', background='blue', foreground='blue', relief='ridge', borderwidth=5, height=400)
bottom_frame = ttk.Frame(root, style='bottom.TFrame')
bottom_frame.pack(expand=False, fill='x', side='bottom', anchor='s', padx=5, pady=5)

root.mainloop()
