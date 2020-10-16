import sys
import time
import multiprocessing as mp
import multiprocessing.queues as mpq

from threading import Thread
from tkinter import *

'''-------------------------------------------------------------------'''
'''                SUBCLASSING THE MULTIPROCESSING QUEUE              '''
'''                                                                   '''
'''         ..and make it behave as a general stdout io               '''
'''-------------------------------------------------------------------'''
# The StdoutQueue is a Queue that behaves like stdout.
# We will subclass the Queue class from the multiprocessing package
# and give it the typical stdout functions.
#
# (1) First issue
# Subclassing multiprocessing.Queue or multiprocessing.SimpleQueue
# will not work, because these classes are not genuine
# python classes.
# Therefore, you need to subclass multiprocessing.queues.Queue or
# multiprocessing.queues.SimpleQueue . This issue is known, and is not
# the reason for asking this question. But I mention it here, for
# completeness.
#
# (2) Second issue
# There is another problem that arises only in Python V5 (and beyond).
# When subclassing multiprocessing.queues.Queue, you have to provide
# a 'multiprocessing context'. Not doing that, leads to an obscure error
# message, which is in fact the main topic of this question. Darth Kotik
# solved it.
# His solution is visible in this code:
class StdoutQueue(mpq.Queue):

    def __init__(self,*args,**kwargs):
        ctx = mp.get_context()
        super(StdoutQueue, self).__init__(*args, **kwargs, ctx=ctx)

    def write(self,msg):
        self.put(msg)

    def flush(self):
        sys.__stdout__.flush()


'''-------------------------------------------------------------------'''
'''                           TEST SETUP                              '''
'''-------------------------------------------------------------------'''

# This function takes the text widget and a queue as inputs.
# It functions by waiting on new data entering the queue, when it
# finds new data it will insert it into the text widget.
def text_catcher(text_widget,queue):
    while True:
        text_widget.insert(END, queue.get())


def test_child(q):
    # This line only redirects stdout inside the current process
    sys.stdout = q
    # or sys.stdout = sys.__stdout__ if you want to print the child to the terminal
    print('child running')

def test_parent(q):
    # Again this only redirects inside the current (main) process
    # commenting this like out will cause only the child to write to the widget
    sys.stdout = q
    print('parent running')
    time.sleep(0.5)
    mp.Process(target=test_child,args=(q,)).start()

if __name__ == '__main__':
    gui_root = Tk()
    gui_txt = Text(gui_root)
    gui_txt.pack()
    q = StdoutQueue()
    gui_btn = Button(gui_root, text='Test', command=lambda:test_parent(q),)
    gui_btn.pack()

    # Instantiate and start the text monitor
    monitor = Thread(target=text_catcher,args=(gui_txt,q))
    monitor.daemon = True
    monitor.start()

    gui_root.mainloop()
