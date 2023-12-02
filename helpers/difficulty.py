"""Increases the difficulty of the game over time"""
import time

__start_time = time.time()


def get_global_speed_modifier() -> float:
    """Returns the global speed modifier"""
    elapsed_time = time.time() - __start_time
    new_speed_modifier = min(1.0 + (elapsed_time / 30.0), 10)
    return new_speed_modifier
