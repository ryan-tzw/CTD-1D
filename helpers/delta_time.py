# pylint: disable=global-statement
import time

delta_time = 0
end_time = 0
start_time = 0


def update_delta_time():
    global delta_time
    delta_time = (start_time - end_time) * 100


def set_start_time():
    global start_time
    start_time = time.time()


def set_end_time():
    global end_time
    end_time = time.time()
