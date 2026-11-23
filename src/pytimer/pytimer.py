"""
pytimer.py
"""


import time


class Timer:
    def __init__(self, do_print=True, do_title=None):
        self.start_time: float | None = None
        self.end_time: float | None = None
        self.print = do_print
        self.title = do_title

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, itype, value, traceback):
        end_time = time.time()
        self.end_time = end_time
        start_time = self.start_time if self.start_time is not None else end_time
        diff = end_time - start_time
        if self.print:
            if self.title:
                print(f"time taken for [{self.title}]: {diff:.6f} seconds")
            else:
                print(f"time taken: {diff:.6f} seconds")
