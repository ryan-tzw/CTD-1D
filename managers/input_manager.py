"""Modules required"""
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
        self._screen: _Screen = None
        self._keys = ["w", "a", "s", "d"]
        self.pressed = []

    def set_screen(self, screen: _Screen):
        """Provide the turtle screen for binding keys to functions

        Args:
            screen (_Screen): Turtle Screen
        """
        self._screen = screen

    def get_pressed_keys(self):
        return self.pressed

    def get_joystick(self) -> tuple[float, float]:
        vector = Vector(0, 0)

        for key in self.pressed:
            match key:
                case "w":
                    vector.add(Vector(0, 1))
                case "a":
                    vector.add(Vector(-1, 0))
                case "s":
                    vector.add(Vector(0, -1))
                case "d":
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