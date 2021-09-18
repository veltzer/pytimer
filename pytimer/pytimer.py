import time


class Timer:
    def __init__(self, do_print=True, do_title=None):
        self.start_time = None
        self.end_time = None
        self.print = do_print
        self.title = do_title

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, itype, value, traceback):
        self.end_time = time.time()
        diff = self.end_time - self.start_time
        if self.print:
            if self.title:
                print(f"time taken for [{self.title}]: {diff:.6f} seconds")
            else:
                print(f"time taken: {diff:.6f} seconds")
