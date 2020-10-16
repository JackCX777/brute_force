# This code try to show print() in GUI text widget (maybe doesn't work):
import sys
# import gui_tk
#
#
# def print_decorator(print_func):
#     def inner(output_string):
#         try:
#             gui_tk.output_screen.insert('end', output_string)
#             return print_func(output_string)
#         except:
#             return print_func(output_string)
#     return inner
#
# # sys.stdout.write=print_decorator(sys.stdout.write)
# sys.stdout.write=print_decorator(print)