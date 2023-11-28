"""Modules required"""
from turtle import Turtle
from uuid import uuid4
from helpers.bounding_box import BoundingBox


class GameObject:
    """Generic GameObject (can be literally anything)"""

    def __init__(
        self,
        x: int,
        y: int,
        color: str,
        shape: str,
    ) -> None:
        self.uuid = uuid4()
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.height = 20
        self.width = 20
        self.render_priority = 0
        self.boundingbox = BoundingBox(self.x, self.y, self.width, self.height)

    def set_dimensions(self, height: int = 20, width: int = 20):
        """Sets the dimensions of the object"""
        self.height = height
        self.width = width
        self.recalculate_boundingbox()

    def set_render_priority(self, render_priority: int):
        """Sets the render priority. Default = 0

        Args:
            render_priority (int): Integer priority value, larger values take higher priority.
        """
        self.render_priority = render_priority

    def update(self):
        """Generic placeholder update function"""

    def render(self, pen: Turtle):
        """Renders the object on the screen"""
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.shapesize(self.width / 20, self.height / 20)
        pen.color(self.color)
        pen.stamp()

    def recalculate_boundingbox(self):
        """Recalculates the bounding box of the object"""
        self.boundingbox = BoundingBox(self.x, self.y, self.width, self.height)


# class Obstacle(GameObject):
#     def __init__(self, x: int, y: int, color: str, shape: str) -> None:
#         super().__init__(x, y, color, shape)

# def _calculate_boundingbox(self):
#     bb = {
#         "min_x": self.x - self.width / 2,
#         "max_x": self.x + self.width / 2,
#         "min_y": self.y - self.width / 2,
#         "max_y": self.y + self.width / 2,
#     }
#     return bb
