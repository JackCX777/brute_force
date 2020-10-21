# This module contains special MultiprocessStdOutQueue class.
# It is inherited from the multiprocessing.queues.Queue class and extends its functionality
# for special multiprocess queue implementation, that puts sys.stdout messages
# and immediately flushes it one by one.


import multiprocessing
from multiprocessing.queues import Queue as MP_queue
import sys


class MultiprocessStdOutQueue(MP_queue):
    def __init__(self, *args, **kwargs):
        context = multiprocessing.get_context()
        super(MultiprocessStdOutQueue, self).__init__(*args, **kwargs, ctx=context)

    def write(self, msg):
        self.put(msg)

    def flush(self):
        sys.__stdout__.flush()
