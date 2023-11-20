"""Modules required"""
from functools import partial
from classes.helpers.vector import Vector


# TODO: split current InputManager into PlayerMovementController
class InputManager:
    """Class that manages inputs (wow)"""

    def __init__(self, player, screen) -> None:
        self.player = player
        self.screen = screen
        self.direction = Vector(0, 0)

        self.keys_pressed = {
            "w": False,
            "a": False,
            "s": False,
            "d": False,
        }

    def move(self):
        """Moves the Player around with appropriate rotation"""
        self.calculate_rotation()

        if self.direction.get_magnitude() > 0:
            self.player.forward(10)

    def calculate_rotation(self):
        """Calculates rotation according to the direction vector"""
        if self.direction.get_magnitude() > 0:
            self.player.setheading(self.direction.get_rotation())

    def add_to_direction(self, x, y):
        """Adds x and y to the direction vector

        Args:
            x (float): value to add to the x direction
            y (float): value to add to the y direction
        """
        self.direction.add(Vector(x, y))

    def subtract_from_direction(self, x, y):
        """Subtracts x and y from the direction vector

        Args:
            x (float): value to subtract from the x direction
            y (float): value to subtract from the y direction
        """
        self.direction.subtract(Vector(x, y))

    def press_key(self, key):
        """When movement keys are pressed

        Args:
            key (str): string containing the key pressed
        """
        if self.keys_pressed[key] is True:
            return

        match key:
            case "w":
                self.add_to_direction(0, 1)
                self.keys_pressed["w"] = True
            case "a":
                self.add_to_direction(-1, 0)
                self.keys_pressed["a"] = True
            case "s":
                self.add_to_direction(0, -1)
                self.keys_pressed["s"] = True
            case "d":
                self.add_to_direction(1, 0)
                self.keys_pressed["d"] = True

    def release_key(self, key):
        """When movement keys are released

        Args:
            key (str): string containing the key released
        """
        match key:
            case "w":
                self.subtract_from_direction(0, 1)
                self.keys_pressed["w"] = False
            case "a":
                self.subtract_from_direction(-1, 0)
                self.keys_pressed["a"] = False
            case "s":
                self.subtract_from_direction(0, -1)
                self.keys_pressed["s"] = False
            case "d":
                self.subtract_from_direction(1, 0)
                self.keys_pressed["d"] = False

    def setup_keys(self):
        """Sets up the keys required for player input"""
        self.screen.onkeypress(partial(self.press_key, "w"), "w")
        self.screen.onkeypress(partial(self.press_key, "a"), "a")
        self.screen.onkeypress(partial(self.press_key, "s"), "s")
        self.screen.onkeypress(partial(self.press_key, "d"), "d")

        self.screen.onkeyrelease(partial(self.release_key, "w"), "w")
        self.screen.onkeyrelease(partial(self.release_key, "a"), "a")
        self.screen.onkeyrelease(partial(self.release_key, "s"), "s")
        self.screen.onkeyrelease(partial(self.release_key, "d"), "d")
