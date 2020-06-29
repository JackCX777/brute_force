import tkinter as tk
import tkinter.ttk as ttk

# This code will replace tkinter widgets by ttk widgets
# from tkinter import *
# from tkinter.ttk import *

root = tk.Tk()
root.title('Brute force')
root.geometry('800x600+300+100')
root.resizable(True, True)

# Anchor option working only with expand option

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

style.configure('top.TFrame', background='red', foreground='red', relief='sunken', borderwidth=5, height=100)
top_frame = ttk.Frame(root, style='top.TFrame')
top_frame.pack(expand=False, fill='x', side='top', anchor='n')
top_label = ttk.Label(top_frame)
top_image = tk.PhotoImage(file='new_top_pass_img.png')
top_label['image'] = top_image
top_label.pack(expand=False, anchor='center')

style.configure('center.TFrame', background='green', foreground='green', relief='sunken', borderwidth=5, height=100)
center_frame = ttk.Frame(root, style='center.TFrame')
center_frame.pack(expand=True, fill='x', anchor='center', padx=5)

style.configure('bottom.TFrame', background='blue', foreground='blue', relief='sunken', borderwidth=5, height=400)
bottom_frame = ttk.Frame(root, style='bottom.TFrame')
bottom_frame.pack(expand=False, fill='x', side='bottom', anchor='s', padx=5, pady=5)

root.mainloop()
