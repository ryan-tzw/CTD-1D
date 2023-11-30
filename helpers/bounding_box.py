"""Bounding box class"""

class BoundingBox:
    """Stores information about the bounding box"""

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.min_x = x - width / 2
        self.max_x = x + width / 2
        self.min_y = y - height / 2
        self.max_y = y + height / 2