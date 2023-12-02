"""A module containing the Player class"""
from core.generics import GameObject
from helpers import delta_time


class Player(GameObject):
    """The main Player GameObject

    Args:
        GameObject (_type_): _description_
    """

    def __init__(self, x: int, y: int, color: str, shape: str) -> None:
        super().__init__(x, y, color, shape)
        self.dx = 0
        self.dy = 0
        self.health = 100
        self.move_speed = 5
        self.height = 40
        self.width = 40

    def update(self):
        """Updates the Entity's position every frame"""
        self.x += self.dx * delta_time.delta_time
        self.y += self.dy * delta_time.delta_time
        self.recalculate_boundingbox()
