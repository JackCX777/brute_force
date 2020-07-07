import tkinter as tk
import tkinter.ttk as ttk
# This code will replace tkinter widgets by ttk widgets
# from tkinter import *
# from tkinter.ttk import *

# Main window
root = tk.Tk()
root.title('Brute force')
root.geometry('820x600+300+100')
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

# Using tk & ttk:
#
# Widget styles
style = ttk.Style()
# style.configure('top.TFrame', background='red', foreground='red', relief='sunken', borderwidth=5, height=100)
style.configure('top.TFrame', height=100)
style.configure('top.TLabel')
# style.configure('center.TFrame', background='green', foreground='green', relief='sunken', borderwidth=5, height=100)
style.configure('center.TFrame', height=100)
style.configure('my.TFrame')
style.configure('Horizontal.TProgressbar')
style.configure('main.TLabelframe', sticky='nsew', borderwidth=5, relief='groove')
style.configure('my.TLabelframe', sticky='n'+'s'+'w'+'e', borderwidth=1)
style.configure('my.TLabel', padx=1, sticky='w')
style.configure('my.TEntry')
style.configure('my.TRadiobutton')
style.configure('start.TButton', foreground='green')
style.configure('stop.TButton', foreground='red')
# style.configure('bottom.TFrame', background='blue', foreground='blue', relief='sunken', borderwidth=5, height=400)
style.configure('bottom.TFrame', height=400)

# Top frame
# Top frame
top_frame = ttk.Frame(root, style='top.TFrame')
top_frame.pack(expand=False, fill='x', side='top', anchor='n')
# Top label & image
top_label = ttk.Label(top_frame, style='top.TLabel')
top_image = tk.PhotoImage(file='new_top_pass_img800.png')
top_label['image'] = top_image
top_label.pack(expand=False, anchor='center')

# Center frame
# Center frame
center_frame = ttk.Frame(root, style='center.TFrame')
center_frame.pack(expand=True, fill='both', anchor='center')
# Server options Labelframes
server_options_frame = ttk.Labelframe(center_frame, text='Server options', style='main.TLabelframe')
server_options_frame.rowconfigure(0, weight=1)
server_options_frame.columnconfigure(0, weight=1)
server_options_frame.grid(row=0, column=0, sticky='n'+'s'+'e'+'w')
server_frame = ttk.Labelframe(server_options_frame, text='Server', style='my.TLabelframe')
server_frame.rowconfigure(0, weight=1)
server_frame.columnconfigure(0, weight=1)
server_frame.grid(row=0, column=0, sticky='n'+'s'+'e'+'w')
auth_frame = ttk.Labelframe(server_options_frame, text='Auth format', style='my.TLabelframe')
auth_frame.rowconfigure(0, weight=1)
auth_frame.columnconfigure(1, weight=1)
auth_frame.grid(row=0, column=1, sticky='n'+'s'+'e'+'w')
test_server_frame = ttk.Labelframe(server_options_frame, text='Test server', style='my.TLabelframe')
test_server_frame.rowconfigure(0, weight=1)
test_server_frame.columnconfigure(2, weight=1)
test_server_frame.grid(row=0, column=2, sticky='n'+'s'+'e'+'w')
# Server options labels
protocol_label = ttk.Label(server_frame, text='Protocol', style='my.TLabel')
protocol_label.rowconfigure(0, weight=1)
protocol_label.columnconfigure(0, weight=1)
node_label = ttk.Label(server_frame, text='Node', style='my.TLabel')
node_label.rowconfigure(1, weight=1)
node_label.columnconfigure(0, weight=1)
port_label = ttk.Label(server_frame, text='Port', style='my.TLabel')
port_label.rowconfigure(2, weight=1)
port_label.columnconfigure(0, weight=1)
path_label = ttk.Label(server_frame, text='Path', style='my.TLabel')
path_label.rowconfigure(3, weight=1)
path_label.columnconfigure(0, weight=1)
protocol_label.grid(row=0, column=0, padx=1, sticky='n'+'s'+'e'+'w')
node_label.grid(row=1, column=0, padx=1, sticky='n'+'s'+'e'+'w')
port_label.grid(row=2, column=0, padx=1, sticky='n'+'s'+'e'+'w')
path_label.grid(row=3, column=0, padx=1, sticky='n'+'s'+'e'+'w')
# Server options entries
protocol_entry = ttk.Entry(server_frame, style='my.TEntry', font='Menlo 12')
protocol_entry.rowconfigure(0, weight=1)
protocol_entry.columnconfigure(1, weight=1)
node_entry = ttk.Entry(server_frame, style='my.TEntry', font='Menlo 12')
node_entry.rowconfigure(1, weight=1)
node_entry.columnconfigure(1, weight=1)
port_entry = ttk.Entry(server_frame, style='my.TEntry', font='Menlo 12')
port_entry.rowconfigure(2, weight=1)
port_entry.columnconfigure(1, weight=1)
path_entry = ttk.Entry(server_frame, style='my.TEntry', font='Menlo 12')
path_entry.rowconfigure(3, weight=1)
path_entry.columnconfigure(1, weight=1)
protocol_entry.grid(row=0, column=1, sticky='n'+'s'+'e'+'w')
node_entry.grid(row=1, column=1, sticky='n'+'s'+'e'+'w')
port_entry.grid(row=2, column=1, sticky='n'+'s'+'e'+'w')
path_entry.grid(row=3, column=1,sticky='n'+'s'+'e'+'w')
# Server options radiobuttons
auth_rbutton_var = tk.IntVar()
auth_rbutton_var.set(1)
auth_rbutton1 = ttk.Radiobutton(auth_frame, text='json', variable=auth_rbutton_var, value=1, style='my.TRadiobutton')
auth_rbutton1.rowconfigure(0, weight=1)
auth_rbutton1.columnconfigure(1, weight=1)
auth_rbutton1.grid(row=0, column=1, sticky='n'+'s'+'e'+'w')
auth_rbutton2 = ttk.Radiobutton(auth_frame, text='data', variable=auth_rbutton_var, value=2, style='my.TRadiobutton')
auth_rbutton2.rowconfigure(1, weight=1)
auth_rbutton2.columnconfigure(1, weight=1)
auth_rbutton2.grid(row=1, column=1, sticky='n'+'s'+'e'+'w')
auth_rbutton3 = ttk.Radiobutton(auth_frame, text='headers', variable=auth_rbutton_var, value=3, style='my.TRadiobutton')
auth_rbutton3.rowconfigure(2, weight=1)
auth_rbutton3.columnconfigure(1, weight=1)
auth_rbutton3.grid(row=2, column=1, sticky='n'+'s'+'e'+'w')
auth_rbutton4 = ttk.Radiobutton(auth_frame, text='other', variable=auth_rbutton_var, value=4, style='my.TRadiobutton')
auth_rbutton4.rowconfigure(3, weight=1)
auth_rbutton4.columnconfigure(1, weight=1)
auth_rbutton4.grid(row=3, column=1, sticky='n'+'s'+'e'+'w')
# Server options test server buttons
test_server_button_on = ttk.Button(test_server_frame, text='run test server', style='start.TButton')
test_server_button_on.rowconfigure(0, weight=1)
test_server_button_on.columnconfigure(0, weight=1)
test_server_button_off = ttk.Button(test_server_frame, text='stop test server', style='stop.TButton')
test_server_button_off.rowconfigure(1, weight=1)
test_server_button_off.columnconfigure(0, weight=1)
test_server_button_on.grid(row=0, column=0, sticky='nsew', ipady=10)
test_server_button_off.grid(row=1, column=0, sticky='nsew', ipady=10)
# Attack options Labelframes
attack_options_frame = ttk.Labelframe(center_frame, text='Attack options', style='main.TLabelframe')
attack_options_frame.rowconfigure(0, weight=1)
attack_options_frame.columnconfigure(1, weight=1)
login_frame = ttk.Labelframe(attack_options_frame, text='Target login', style='my.TLabelframe')
login_frame.rowconfigure(0, weight=1)
login_frame.columnconfigure(0, weight=1)
method_frame = ttk.Labelframe(attack_options_frame, text='Attack method', style='my.TLabelframe')
method_frame.rowconfigure(0, weight=1)
method_frame.columnconfigure(1, weight=1)
attack_frame = ttk.Labelframe(attack_options_frame, text='Attack control', style='my.TLabelframe')
attack_frame.rowconfigure(0, weight=1)
attack_frame.columnconfigure(2, weight=1)
progress_frame = ttk.Frame(attack_options_frame, style='my.TFrame')
progress_frame.rowconfigure(1, weight=1)
progress_frame.columnconfigure(0, weight=1)
attack_options_frame.grid(row=0, column=1, sticky='n'+'s'+'e'+'w')
login_frame.grid(row=0, column=0, sticky='n'+'s'+'e'+'w')
method_frame.grid(row=0, column=1, sticky='n'+'s'+'e'+'w')
attack_frame.grid(row=0, column=2, sticky='n'+'s'+'e'+'w')
progress_frame.grid(row=1, column=0, columnspan=3, sticky='n'+'s'+'e'+'w')
# Attack options labels
login_label = ttk.Label(login_frame, text='Enter target\nlogin or e-mail:', style='my.TLabel')
login_label.rowconfigure(0, weight=1)
login_label.columnconfigure(0, weight=1)
login_label.grid(row=0, column=0, sticky='n'+'s'+'e'+'w')
# Attack options entries
login_entry = ttk.Entry(login_frame, style='my.TEntry', width=10)
login_entry.rowconfigure(1, weight=1)
login_entry.columnconfigure(0, weight=1)
login_entry.grid(row=1, column=0, sticky='n'+'s'+'e'+'w')
# Attack options radiobuttons
attack_rbutton_var = tk.IntVar()
attack_rbutton_var.set(1)
attack_rbutton1 = ttk.Radiobutton(method_frame, text='Smart attack',
                                  variable=attack_rbutton_var, value=1, style='my.TRadiobutton')
attack_rbutton1.rowconfigure(0, weight=1)
attack_rbutton1.columnconfigure(0, weight=1)
attack_rbutton2 = ttk.Radiobutton(method_frame, text='Dictionary attack',
                                  variable=attack_rbutton_var, value=2, style='my.TRadiobutton')
attack_rbutton2.rowconfigure(1, weight=1)
attack_rbutton2.columnconfigure(0, weight=1)
attack_rbutton3 = ttk.Radiobutton(method_frame, text='Brute force attack',
                                  variable=attack_rbutton_var, value=3, style='my.TRadiobutton')
attack_rbutton3.rowconfigure(2, weight=1)
attack_rbutton3.columnconfigure(0, weight=1)
attack_rbutton1.grid(row=0, column=0, sticky='n'+'s'+'e'+'w')
attack_rbutton2.grid(row=1, column=0, sticky='n'+'s'+'e'+'w')
attack_rbutton3.grid(row=2, column=0, sticky='n'+'s'+'e'+'w')
# Attack options buttons
attack_button_on = ttk.Button(attack_frame, text='start attack', style='start.TButton')
attack_button_on.rowconfigure(0, weight=1)
attack_button_on.columnconfigure(0, weight=1)
attack_button_off = ttk.Button(attack_frame, text='stop attack', style='stop.TButton')
attack_button_off.rowconfigure(1, weight=1)
attack_button_off.columnconfigure(0, weight=1)
attack_button_on.grid(row=0, column=0, sticky='n'+'s'+'e'+'w', ipadx=2, ipady=2)
attack_button_off.grid(row=1, column=0, sticky='n'+'s'+'e'+'w', ipadx=2, ipady=2)
# Progress bar
attack_progress = ttk.Progressbar(progress_frame, mode='indeterminate', style='Horizontal.TProgressbar',
                                  length=350, orient=tk.HORIZONTAL, maximum=100)
attack_progress.rowconfigure(0, weight=1)
attack_progress.columnconfigure(0, weight=1)
attack_progress.grid(row=0, column=0, columnspan=3, sticky='n'+'s'+'e'+'w')
attack_progress.start(50)
attack_progress.stop()

# Bottom frame
# Bottom frame
bottom_frame = ttk.Frame(root, style='bottom.TFrame')
bottom_frame.pack(expand=False, fill='x', side='bottom', anchor='s', padx=5, pady=5)
# configure grid manager for text widget good scrolling by y
bottom_frame.rowconfigure(0, weight=1)
# configure grid manager for text widget good extend by x
bottom_frame.columnconfigure(0, weight=1)
# Output screen
output_screen = tk.Text(bottom_frame, bg='#000000', fg='#64c864', font='Menlo 14', wrap='word', padx=7,
                        selectforeground='red', insertbackground='#64c864')
output_screen.rowconfigure(0, weight=1)
output_screen.columnconfigure(0, weight=1)
output_screen.grid(row=0, column=0, sticky='nsew')
# Scrollbar for output screen
yscrollbar = tk.Scrollbar(bottom_frame, orient='vert', command=output_screen.yview)
output_screen['yscrollcommand'] = yscrollbar.set
yscrollbar.rowconfigure(0, weight=1)
yscrollbar.columnconfigure(1, weight=1)
yscrollbar.grid(row=0, column=1, sticky='n'+'s'+'e'+'w')
xscrollbar = tk.Scrollbar(bottom_frame, orient='hor', command=output_screen.xview)
output_screen['xscrollcommand'] = xscrollbar.set
xscrollbar.rowconfigure(1, weight=1)
xscrollbar.columnconfigure(0, weight=1)
xscrollbar.grid(row=1, column=0, sticky='n'+'s'+'e'+'w')

root.mainloop()
