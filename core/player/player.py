"""Required modules"""
from core.generics import Entity


class Player(Entity):
    """The main Player GameObject

    Args:
        GameObject (_type_): _description_
    """

    def __init__(self, x, y, color, shape) -> None:
        super().__init__(x, y, color, shape)
        self.health = 100
        self.move_speed = 10
