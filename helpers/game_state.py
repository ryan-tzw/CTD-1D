"""This module contains the game state variable and functions to set and get it."""
# pylint: disable=global-statement
__game_state: str = "home_screen"


def set_game_state(state: str):
    """Sets the game state to the home screen"""
    global __game_state
    possible_states = ["home_screen", "playing", "game_over"]
    if state in possible_states:
        __game_state = state
    else:
        raise ValueError("Invalid game state.")


def get_game_state() -> str:
    """Returns the current game state"""
    return __game_state
