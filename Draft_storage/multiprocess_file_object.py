import multiprocessing

from io import StringIO
# from os import getpid

class MultiprocessFileObject(object):
    def __init__(self):
        # self.__master = getpid()
        self.__master = multiprocessing.current_process()
        self.__queue = multiprocessing.Manager().Queue()
        self.__buffer = StringIO()
        self.softplace = 0

    def buffer(self):
        if getpid() != self.__master:
        # if multiprocessing.current_process() != self.__master:
            return
        # from Queue import Empty
        from collections import defaultdict
        cache = defaultdict(str)
        # while True:
        #     try:
        #         pid, data = self.__queue.get_nowait()
        #     except Empty:
        #         break
        while True:
            if not self.__queue.empty():
                pid, data = self.__queue.get_nowait()
            else:
                break
            cache[pid] += data
        for pid in sorted(cache):
            self.__buffer.write('%s wrote: %r\n' % (pid, cache[pid]))

    def write(self, data):
        # self.__queue.put((getpid(), data))
        self.__queue.put((multiprocessing.current_process(), data))
    def __iter__(self):
        # getattr doesn't work for iter()
        self.buffer()
        return self.__buffer

    def get_value(self):
        self.buffer()
        self.__buffer.getvalue()

    def flush(self):
        # meaningless
        pass