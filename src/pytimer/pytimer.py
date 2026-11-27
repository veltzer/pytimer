"""
pytimer.py
"""


import time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types import TracebackType


class Timer:
    def __init__(self, *, do_print: bool = True, do_title: str | None = None) -> None:
        self.start_time: float | None = None
        self.end_time: float | None = None
        self.print = do_print
        self.title = do_title

    def __enter__(self) -> None:
        self.start_time = time.time()

    def __exit__(self, itype: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None) -> None:
        end_time = time.time()
        self.end_time = end_time
        start_time = self.start_time if self.start_time is not None else end_time
        diff = end_time - start_time
        if self.print:
            if self.title:
                print(f"time taken for [{self.title}]: {diff:.6f} seconds")
            else:
                print(f"time taken: {diff:.6f} seconds")
