# pylint: disable=global-statement
game_state: str = "home_screen"


def set_game_state(state: str):
    """Sets the game state to the home screen"""
    global game_state
    possible_states = ["home_screen", "playing", "game_over"]
    if state in possible_states:
        game_state = state
    else:
        raise ValueError("Invalid game state.")
