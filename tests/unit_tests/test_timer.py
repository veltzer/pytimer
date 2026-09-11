"""Behavioural tests for pytimer's Timer context manager."""

import unittest

from pytimer.pytimer import Timer


class TimerTests(unittest.TestCase):
    def test_times_are_none_before_use(self):
        timer = Timer(do_print=False)
        self.assertIsNone(timer.start_time)
        self.assertIsNone(timer.end_time)

    def test_context_sets_start_and_end(self):
        timer = Timer(do_print=False)
        with timer:
            pass
        self.assertIsNotNone(timer.start_time)
        self.assertIsNotNone(timer.end_time)

    def test_end_is_not_before_start(self):
        timer = Timer(do_print=False)
        with timer:
            pass
        self.assertGreaterEqual(timer.end_time, timer.start_time)

    def test_title_is_stored(self):
        timer = Timer(do_print=False, do_title="phase one")
        self.assertEqual(timer.title, "phase one")

    def test_default_print_flag_is_true(self):
        self.assertTrue(Timer().print)
