"""Modules required"""
from turtle import Turtle
from uuid import uuid4


class GameObject:
    """Generic GameObject (can be literally anything)"""

    def __init__(self, x: int, y: int, color: str, shape: str) -> None:
        self.uuid = uuid4()
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape

    def render(self, pen: Turtle):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()


class Entity(GameObject):
    """Generic Entity that can move"""

    def __init__(self, x: int, y: int, color: str, shape: str) -> None:
        super().__init__(x, y, color, shape)
        self.dx = 0
        self.dy = 0

    def update(self):
        """Updates the Entity's position every frame"""
        self.x += self.dx
        self.y += self.dy
