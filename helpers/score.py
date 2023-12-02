"""Score module. Used to keep track of the player's score"""
# pylint: disable=global-statement, invalid-name

__score: int = 0


def get_score() -> int:
    """Returns the current score"""
    return __score


def add_score() -> None:
    """Adds 1 to the score"""
    global __score
    __score += 1


def reset_score() -> None:
    """Resets the score to 0"""
    global __score
    __score = 0
