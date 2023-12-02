"""A module containing the InputManager class"""
from functools import partial
from turtle import _Screen
from helpers.vector import Vector


class InputManager:
    """Class that manages inputs (wow)"""

    _instance = None

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self._screen: _Screen
        self._keys = ["w", "a", "s", "d", "Left", "Right", "Up", "Down"]
        self.pressed = []

    def set_screen(self, screen: _Screen):
        """Provide the turtle screen for binding keys to functions

        Args:
            screen (_Screen): Turtle Screen
        """
        self._screen = screen

    def get_normalised_vector(self) -> tuple[float, float]:
        """Returns a Vector representing the cumulative direction of the WASD keys

        Returns:
            tuple[float, float]: tuple with x and y components of the vector
        """
        vector = Vector(0, 0)

        for key in self.pressed:
            match key:
                case "w" | "Up":
                    vector.add(Vector(0, 1))
                case "a" | "Left":
                    vector.add(Vector(-1, 0))
                case "s" | "Down":
                    vector.add(Vector(0, -1))
                case "d" | "Right":
                    vector.add(Vector(1, 0))

        vector.normalize()
        return vector.x, vector.y

    def press_key(self, key):
        """When key is pressed

        Args:
            key (str): Key pressed
        """
        if key not in self.pressed:
            self.pressed.append(key)

    def release_key(self, key):
        """When key is released

        Args:
            key (str): Key pressed
        """
        self.pressed.remove(key)

    def setup_keys(self):
        """Sets up the keys required for player input"""
        for key in self._keys:
            self._screen.onkeypress(partial(self.press_key, key), key)
            self._screen.onkeyrelease(partial(self.release_key, key), key)


if __name__ == "__main__":
    print("Run the code from the main.py file tyvm")
