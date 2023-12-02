"""Delta time module. Used to calculate the time between frames"""
# pylint: disable=global-statement, invalid-name
import time

__delta_time: float = 0
__end_time: float = 0
__start_time: float = 0


def get_delta_time() -> float:
    """Returns delta time"""
    return __delta_time


def update_delta_time():
    """Update delta time"""
    global __delta_time
    speed_modifier = 100
    __delta_time = (__start_time - __end_time) * speed_modifier


def set_start_time():
    """Set start time"""
    global __start_time
    __start_time = time.time()


def set_end_time():
    """Set end time"""
    global __end_time
    __end_time = time.time()
