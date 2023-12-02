"""Score module. Used to keep track of the player's score"""
# pylint: disable=global-statement
score = 0


def add_score() -> None:
    global score
    score += 1
