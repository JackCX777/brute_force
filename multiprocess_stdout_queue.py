import multiprocessing
from multiprocessing.queues import Queue as MP_queue
import sys


class MultiprocessStdOutQueue(MP_queue):
    def __init__(self, *args, **kwargs):
        context = multiprocessing.get_context()
        super(MultiprocessStdOutQueue, self).__init__(*args, **kwargs, ctx=context)

    def write(self, msg):
        self.put_nowait(msg)

    def flush(self):
        sys.__stdout__.flush()
