"""Modules required"""
import math


class Vector:
    """Helper class for defining vectors"""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def add(self, other: "Vector") -> None:
        """Adds 2 vectors together

        Args:
            other (Vector): Another Vector
        """
        self.x += other.x
        self.y += other.y

    def subtract(self, other: "Vector"):
        """Subtracts other vector from current vector

        Args:
            other (Vector): Another Vector
        """
        self.x -= other.x
        self.y -= other.y

    def multiply(self, scalar: float):
        """Multiplies current vector by some factor

        Args:
            scalar (float): Scalar value to multiply by
        """
        self.x *= scalar
        self.y *= scalar

    def get_magnitude(self):
        """Returns the magnitude of the vector

        Returns:
            float: magnitude of the vector
        """
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        """Normalises the current vector"""
        mag = self.get_magnitude()
        if mag != 0:
            self.x /= mag
            self.y /= mag

    def get_rotation(self):
        """Gets the angle the vector makes with the x-axis

        Returns:
            float: angle that the vector forms with the x-axis
        """
        angle = math.degrees(math.atan2(self.y, self.x))
        if angle < 0:
            angle += 360
        return angle


if __name__ == "__main__":
    print("Run the code from the main.py file tyvm")
