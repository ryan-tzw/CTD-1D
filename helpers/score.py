# pylint: disable=global-statement
score = 0


def add_score() -> None:
    global score
    score += 1
