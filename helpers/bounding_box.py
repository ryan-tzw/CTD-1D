"""Bounding box class"""


class BoundingBox:
    """Stores information about the bounding box"""

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self._tolerance = 0.8
        self._delta_width = self._tolerance * width / 2
        self._delta_height = self._tolerance * height / 2

        self.min_x = x - self._delta_width
        self.max_x = x + self._delta_width
        self.min_y = y - self._delta_height
        self.max_y = y + self._delta_height
