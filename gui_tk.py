import tkinter as tk
import tkinter.ttk as ttk
# This code will replace tkinter widgets by ttk widgets
# from tkinter import *
# from tkinter.ttk import *

# This for run test_server_WSGI.py by click button
from test_server_WSGI import start_app as application_server
import multiprocessing

# This is in order to implement a queue for data exchange between processes using a thread.
from threading import Thread
from multiprocess_stdout_queue import MultiprocessStdOutQueue
import time

import json
import server_settings
import substitution_password_attacks
import brute_force_password_attacks
import attack_plans


# global vars:
test_server_proc = None
attack_proc = None
attack_in_progress_flag = False
stdout_capture_thread = None
thread_stop_flag = False


# Command functions
def queue_catcher(captured_queue, screen):
    global thread_stop_flag
    while not captured_queue.empty():
        if not thread_stop_flag:
            # time.sleep(0.001)
            # print(captured_queue.get())
            screen.insert('end', captured_queue.get_nowait() + '\n')
            screen.see('end')
        else:
            captured_queue.flush()
            captured_queue.all_tasks_done()
            captured_queue.cancel_join_thread()
            break
    captured_queue.close()
    screen.insert('end', ' End of attack.\n')
    thread_stop_flag = True
    attack_button_off_clicked()


def test_server_button_on_clicked():
    global test_server_proc
    protocol_var.set('http')
    node_var.set('127.0.0.1')
    port_var.set('5000')
    path_var.set('auth')
    auth_rbutton_var.set(1)
    # pass_len_var.set(0)
    style.configure('server.TEntry', background='lightgrey')
    protocol_entry['state'] = 'disabled'
    node_entry['state'] = 'disabled'
    port_entry['state'] = 'disabled'
    path_entry['state'] = 'disabled'
    auth_rbutton1['state'] = 'disabled'
    auth_rbutton2['state'] = 'disabled'
    auth_rbutton3['state'] = 'disabled'
    auth_rbutton4['state'] = 'disabled'
    if test_server_proc is not None:
        if test_server_proc.is_alive():
            output_screen.delete('1.0', 'end')
            output_screen.insert('end', ' Test server already in use!\n')
        else:
            test_server_proc.terminate()
            test_server_proc.join()
            test_server_proc.close()
            test_server_proc = None
            output_screen.delete('1.0', 'end')
            output_screen.insert('end', ' The start of the test server failed.\n Try again!\n')
    else:
        output_screen.delete('1.0', 'end')
        test_server_proc = multiprocessing.Process(target=application_server)
        test_server_proc.start()
        output_screen.insert('end', ' Test server is up!\n')


def test_server_button_off_clicked():
    global test_server_proc
    protocol_var.set('')
    node_var.set('')
    port_var.set('')
    path_var.set('')
    auth_rbutton_var.set(1)
    style.configure('server.TEntry', background='white')
    protocol_entry['state'] = 'normal'
    node_entry['state'] = 'normal'
    port_entry['state'] = 'normal'
    path_entry['state'] = 'normal'
    auth_rbutton1['state'] = 'normal'
    auth_rbutton2['state'] = 'normal'
    auth_rbutton3['state'] = 'normal'
    auth_rbutton4['state'] = 'normal'
    if test_server_proc is None:
        output_screen.delete('1.0', 'end')
        output_screen.insert('end', ' Test server is not in use!\n')
    elif test_server_proc.is_alive():
        test_server_proc.terminate()
        test_server_proc.join()
        test_server_proc.close()
        test_server_proc = None
        output_screen.delete('1.0', 'end')
        output_screen.insert('end', ' Test server is down!\n')
    else:
        output_screen.delete('1.0', 'end')
        output_screen.insert('end', ' Test server is already stopped!\n')


def attack_button_on_clicked():
    global attack_proc
    global attack_in_progress_flag
    global stdout_capture_thread
    global thread_stop_flag
    # Checking for any attacks in progress
    if attack_in_progress_flag:
        output_screen.insert('end', ' First you have to stop the current attack!\n')
    else:
        output_screen.delete('1.0', 'end')
        # Checking target server settings and overwrite server_settings.json file
        start_attack_flag = False
        auth_format_flag = False
        login_flag = False
        protocol_flag = False
        node_flag = False
        port_flag = False
        path_flag = False
        pass_len_flag = False
        with open('server_settings.json', 'r') as settings_server_file_:
            set_serv_dict = json.load(settings_server_file_)
            # 1 Checking target server auth format:
            if auth_rbutton_var.get() == 1:
                set_serv_dict['net_query'] = 'json'
                auth_format_flag = True
            elif auth_rbutton_var.get() == 2:
                # set_serv_dict['net_query'] = 'data'
                auth_format_flag = False
                output_screen.insert('end', ' Test server supports only json authorisation!\n'
                                     + 'You can use this program only with test server!\n')
            elif auth_rbutton_var.get() == 3:
                # set_serv_dict['net_query'] = 'headers'
                auth_format_flag = False
                output_screen.insert('end', ' Test server supports only json authorisation!\n'
                                     + 'You can use this program only with test server!\n')
            elif auth_rbutton_var.get() == 4:
                # set_serv_dict['net_query'] = 'other'
                auth_format_flag = False
                output_screen.insert('end', ' Test server supports only json authorisation!\n'
                                     + 'You can use this program only with test server!\n')
            # 2 Checking target server login:
            if login_var.get() == '':
                output_screen.insert('end', ' Login entry field is empty!\n')
                login_flag = False
            elif login_var.get() not in ['admin', 'cat', 'jack']:
                output_screen.insert('end', ' Test server supports only three logins:\n'
                                     + '\"admin\", \"cat\" or \"jack\"!\n'
                                     + 'You can use this program only with test server!\n')
                login_flag = False
            else:
                set_serv_dict['server_login'] = login_var.get()
                login_flag = True
            # 3 Checking target server protocol
            if protocol_var.get() == '':
                output_screen.insert('end', ' Protocol entry field is empty!\n')
                protocol_flag = False
            elif protocol_var.get() != 'http':
                output_screen.insert('end', ' Test server uses http protocol only!\n')
                protocol_flag = False
            else:
                set_serv_dict['net_protocol'] = protocol_var.get()
                protocol_flag = True
            # 4 Checking target server node:
            if node_var.get() == '':
                output_screen.insert('end', ' Node entry field is empty!\n')
                node_flag = False
            elif node_var.get() != '127.0.0.1':
                output_screen.insert('end', ' Test server node is 127.0.0.1!\n'
                                     + 'You can use this program only with test server!\n')
                node_flag = False
            else:
                set_serv_dict['net_node'] = node_var.get()
                node_flag = True
            # 5 Checking target server port:
            if port_var.get() == '':
                output_screen.insert('end', ' Port entry field is empty!\n')
                port_flag = False
            elif port_var.get() != '5000':
                output_screen.insert('end', ' Test server uses 5000 port!\n')
                port_flag = False
            else:
                set_serv_dict['net_port'] = port_var.get()
                port_flag = True
            # 6 Checking target server path:
            if path_var.get() == '':
                output_screen.insert('end', ' Path entry field is empty!\n')
                path_flag = False
            elif path_var.get() != 'auth':
                output_screen.insert('end', ' Test server authorisation path is auth!\n')
                path_flag = False
            else:
                set_serv_dict['net_path'] = path_var.get()
                path_flag = True
            # 7 Checking target server password length:
            if pass_len_var.get().isdigit():
                set_serv_dict['password_length'] = pass_len_var.get()
                pass_len_flag = True
            else:
                output_screen.insert(
                    'end', ' Password length entry field supports only numbers and should not be empty!\n'
                           + 'If you have no idea about the length of the password, use 0.\n'
                )
                pass_len_flag = False
        # Checking for server settings and starting selected attack:
        if auth_format_flag\
                and login_flag\
                and protocol_flag\
                and node_flag\
                and port_flag\
                and path_flag\
                and pass_len_flag:
            start_attack_flag = True
        else:
            start_attack_flag = False
        if start_attack_flag:
            with open('server_settings.json', 'w') as settings_server_file_w:
                json.dump(set_serv_dict, settings_server_file_w, indent=4, sort_keys=False)
            stdout_queue = MultiprocessStdOutQueue()
            if attack_rbutton_var.get() == 1:
                attack_proc = multiprocessing.Process(target=attack_plans.smart_password_attack,
                                                      name='attack_process',
                                                      args=(substitution_password_attacks.brute_by_target_info,
                                                            substitution_password_attacks.brute_by_password_list,
                                                            brute_force_password_attacks.brute_force_password,
                                                            stdout_queue,
                                                            )
                                                      )
            elif attack_rbutton_var.get() == 2:
                attack_proc = multiprocessing.Process(target=attack_plans.password_attack_by_target_info_only,
                                                      name='attack_process',
                                                      args=(substitution_password_attacks.brute_by_target_info,
                                                            stdout_queue,
                                                            )
                                                      )
            elif attack_rbutton_var.get() == 3:
                attack_proc = multiprocessing.Process(target=attack_plans.password_attack_by_brute_force_only,
                                                      name='attack_process',
                                                      args=(brute_force_password_attacks.brute_force_password,
                                                            stdout_queue,
                                                            )
                                                      )
            if attack_proc is not None:
                if stdout_capture_thread is not None:
                    stdout_capture_thread.join()
                stdout_capture_thread = None
                attack_in_progress_flag = True
                attack_progress.start()
                output_screen.insert('end', ' Starting attack:\n')
                attack_proc.start()
                time.sleep(0.3)
                thread_stop_flag = False
                stdout_capture_thread = Thread(target=queue_catcher, name='capture_thread',
                                               args=(stdout_queue, output_screen,))
                # stdout_capture_thread.daemon = True
                stdout_capture_thread.start()
            else:
                output_screen.insert('end', ' Something wrong with attack process!\n'
                                     + 'Try again!\n')
        else:
            output_screen.insert('end', ' Unable to launch attack!\n')


def attack_button_off_clicked():
    global attack_proc
    global attack_in_progress_flag
    global thread_stop_flag
    global stdout_capture_thread
    thread_stop_flag = True
    if attack_proc is None:
        output_screen.delete('1.0', 'end')
        output_screen.insert('end', ' No active attacks!\n')
    else:
        if attack_proc.is_alive():
            attack_proc.terminate()
            attack_proc.join()
            # output_screen.delete('1.0', 'end')
            output_screen.insert('end', ' Attack stopped by user\n')
        attack_proc.close()
        attack_proc = None
    attack_progress.stop()
    attack_in_progress_flag = False


def x_main_window():
    global test_server_proc
    global attack_proc
    global stdout_capture_thread
    global thread_stop_flag
    thread_stop_flag = True
    if stdout_capture_thread is not None:
        time.sleep(0.3)
        stdout_capture_thread.join()
        stdout_capture_thread = None
    if attack_proc is not None:
        attack_proc.terminate()
        attack_proc.join()
        attack_proc.close()
        attack_proc = None
    if test_server_proc is not None:
        test_server_proc.terminate()
        test_server_proc.join()
        test_server_proc.close()
        test_server_proc = None
    root.destroy()


# Main window
root = tk.Tk()
root.title('Brute force')
root.geometry('820x600+300+100')
root.resizable(False, False)

# Anchor option working only with expand option
#
# It makes widget stretchable:
# widget.rowconfigure(0, weight=1)
# widget.columnconfigure(0, weight=1)
# widget.grid(sticky='n'+'s'+'e'+'w')

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
style.configure('my.TLabelframe', sticky='n' + 's' + 'e' + 'w', borderwidth=1)
style.configure('my.TLabel', padx=1, sticky='w')
style.configure('server.TEntry')
style.configure('login.TEntry')
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
server_options_frame.grid(row=0, column=0, sticky='n')
server_frame = ttk.Labelframe(server_options_frame, text='Server', style='my.TLabelframe')
server_frame.grid(row=0, column=0, sticky='n')
auth_frame = ttk.Labelframe(server_options_frame, text='Auth format', style='my.TLabelframe')
auth_frame.grid(row=0, column=1, sticky='n')
test_server_frame = ttk.Labelframe(server_options_frame, text='Test server', style='my.TLabelframe')
test_server_frame.grid(row=0, column=2, sticky='n')
# Server options labels
protocol_label = ttk.Label(server_frame, text='Protocol', style='my.TLabel')
node_label = ttk.Label(server_frame, text='Node', style='my.TLabel')
port_label = ttk.Label(server_frame, text='Port', style='my.TLabel')
path_label = ttk.Label(server_frame, text='Path', style='my.TLabel')
protocol_label.grid(row=0, column=0, padx=1, sticky='w')
node_label.grid(row=1, column=0, padx=1, sticky='w')
port_label.grid(row=2, column=0, padx=1, sticky='w')
path_label.grid(row=3, column=0, padx=1, sticky='w')
# Server options entries
protocol_var = tk.StringVar()
protocol_entry = ttk.Entry(server_frame, style='server.TEntry', font='Menlo 12', textvariable=protocol_var)
# protocol_entry.insert(tk.END, 'http')
node_var = tk.StringVar()
node_entry = ttk.Entry(server_frame, style='server.TEntry', font='Menlo 12', textvariable=node_var)
port_var = tk.StringVar()
port_entry = ttk.Entry(server_frame, style='server.TEntry', font='Menlo 12', textvariable=port_var)
path_var = tk.StringVar()
path_entry = ttk.Entry(server_frame, style='server.TEntry', font='Menlo 12', textvariable=path_var)
protocol_entry.grid(row=0, column=1)
node_entry.grid(row=1, column=1)
port_entry.grid(row=2, column=1)
path_entry.grid(row=3, column=1)
# Server options radiobuttons
auth_rbutton_var = tk.IntVar()
auth_rbutton_var.set(1)
auth_rbutton1 = ttk.Radiobutton(auth_frame, text='json', variable=auth_rbutton_var, value=1, style='my.TRadiobutton')
auth_rbutton1.grid(row=0, column=1, sticky='w')
auth_rbutton2 = ttk.Radiobutton(auth_frame, text='data', variable=auth_rbutton_var, value=2, style='my.TRadiobutton')
auth_rbutton2.grid(row=1, column=1, sticky='w')
auth_rbutton3 = ttk.Radiobutton(auth_frame, text='headers', variable=auth_rbutton_var, value=3, style='my.TRadiobutton')
auth_rbutton3.grid(row=2, column=1, sticky='w')
auth_rbutton4 = ttk.Radiobutton(auth_frame, text='other', variable=auth_rbutton_var, value=4, style='my.TRadiobutton')
auth_rbutton4.grid(row=3, column=1, sticky='w')
# Server options test server buttons
test_server_button_on = ttk.Button(test_server_frame, text='run test server', style='start.TButton',
                                   command=test_server_button_on_clicked)
test_server_button_off = ttk.Button(test_server_frame, text='stop test server', style='stop.TButton',
                                    command=test_server_button_off_clicked)
test_server_button_on.grid(row=0, column=0, sticky='nsew', ipady=10)
test_server_button_off.grid(row=1, column=0, sticky='nsew', ipady=10)
# Attack options Labelframes
attack_options_frame = ttk.Labelframe(center_frame, text='Attack options', style='main.TLabelframe')
login_frame = ttk.Labelframe(attack_options_frame, text='Target login', style='my.TLabelframe')
pass_len_frame = ttk.Labelframe(attack_options_frame, text='Password', style='my.TLabelframe')
method_frame = ttk.Labelframe(attack_options_frame, text='Attack method', style='my.TLabelframe')
attack_frame = ttk.Frame(attack_options_frame, style='my.TFrame')
attack_options_frame.grid(row=0, column=1, sticky='n')
login_frame.grid(row=0, column=0, sticky='n')
pass_len_frame.grid(row=0, column=1, sticky='n')
method_frame.grid(row=0, column=2, sticky='n')
attack_frame.grid(row=1, column=0, columnspan=3, sticky='ew')
attack_options_frame.rowconfigure(0, weight=1)
attack_options_frame.columnconfigure(0, weight=1)
# Attack options labels
login_label = ttk.Label(login_frame, text='Enter target\nlogin or e-mail:', style='my.TLabel')
login_label.grid(row=0, column=0)
pass_len_label = ttk.Label(pass_len_frame, text='Min password\nlength:', style='my.TLabel')
pass_len_label.grid(row=0, column=0)
# Attack options entries
login_var = tk.StringVar()
login_entry = ttk.Entry(login_frame, style='login.TEntry', width=10, textvariable=login_var)
login_entry.grid(row=1, column=0)
pass_len_var = tk.StringVar()
pass_len_var.set('0')
pass_len_entry = ttk.Entry(pass_len_frame, style='login.TEntry', width=10, textvariable=pass_len_var)
pass_len_entry.grid(row=2, column=0, sticky='w')
# Attack options radiobuttons
attack_rbutton_var = tk.IntVar()
attack_rbutton_var.set(1)
attack_rbutton1 = ttk.Radiobutton(method_frame, text='Smart attack',
                                  variable=attack_rbutton_var, value=1, style='my.TRadiobutton')
attack_rbutton2 = ttk.Radiobutton(method_frame, text='Dictionary attack',
                                  variable=attack_rbutton_var, value=2, style='my.TRadiobutton')
attack_rbutton3 = ttk.Radiobutton(method_frame, text='Brute force attack',
                                  variable=attack_rbutton_var, value=3, style='my.TRadiobutton')
attack_rbutton1.grid(row=0, column=0, sticky='w')
attack_rbutton2.grid(row=1, column=0, sticky='w')
attack_rbutton3.grid(row=2, column=0, sticky='w')
# Attack options buttons
attack_button_on = ttk.Button(attack_frame, text='start attack', style='start.TButton',
                              command=attack_button_on_clicked)
attack_button_off = ttk.Button(attack_frame, text='stop attack', style='stop.TButton',
                               command=attack_button_off_clicked)
attack_button_on.grid(row=0, column=0, sticky='w' + 'e', padx=5, ipadx=30)
attack_button_off.grid(row=0, column=1, sticky='w' + 'e', padx=5, ipadx=30)
# Progress bar
progress_frame = ttk.Frame(center_frame, style='my.TFrame')
progress_frame.grid(row=1, column=0, columnspan=2, sticky='ew')
attack_progress = ttk.Progressbar(progress_frame, mode='indeterminate', style='Horizontal.TProgressbar',
                                  length=800, orient=tk.HORIZONTAL, maximum=100)
attack_progress.grid(row=0, column=0, padx=10, sticky='ew')
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
                        selectforeground='red', insertbackground='#64c864', state='normal')
output_screen.grid(row=0, column=0, sticky='nsew')
# Scrollbar for output screen
yscrollbar = tk.Scrollbar(bottom_frame, orient='vert', command=output_screen.yview)
output_screen['yscrollcommand'] = yscrollbar.set
yscrollbar.grid(row=0, column=1, sticky='ns')
xscrollbar = tk.Scrollbar(bottom_frame, orient='hor', command=output_screen.xview)
output_screen['xscrollcommand'] = xscrollbar.set
xscrollbar.grid(row=1, column=0, sticky='ew')

# This code call function x_main_window()
# when user close main window by clicking x
root.protocol('WM_DELETE_WINDOW', x_main_window)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    root.mainloop()
