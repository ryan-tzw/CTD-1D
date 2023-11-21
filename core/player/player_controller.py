"""Required modules"""
from managers.input_manager import InputManager
from core.player.player import Player


class PlayerController:
    """Separated logic for controlling the Player"""

    def __init__(self, player: Player) -> None:
        self.player = player
        self._input_manager = InputManager()

    def update(self):
        """Updates the Player's change in position every frame"""
        x, y = self._input_manager.get_joystick()
        self.player.dx = x * self.player.move_speed
        self.player.dy = y * self.player.move_speed