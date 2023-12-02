"""A module containing the PlayerController class"""
from managers.input_manager import InputManager
from core.player.player import Player


class PlayerController:
    """Separated logic for controlling the Player"""

    def __init__(self, player: Player) -> None:
        self.player = player
        self._input_manager = InputManager()

    def move(self):
        """Updates the Player's change in position every frame"""
        x, y = self._input_manager.get_normalised_vector()
        self.player.dx = x * self.player.move_speed
        self.player.dy = y * self.player.move_speed

    def update(self):
        self.move()
