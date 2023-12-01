"""Modules required"""
# pylint: disable=no-name-in-module
from random import randint
from turtle import window_height, window_width
from core.generics import Obstacle
from managers.collision_manager import CollisionManager
from managers.game_manager import GameManager


class SpawnManager:
    """Spawns falling obstacles"""

    def __init__(
        self, game_manager: GameManager, collision_manager: CollisionManager
    ) -> None:
        self._game_manager = game_manager
        self._collision_manager = collision_manager
        self._obstacles = []
        self.countdown = 0

    def update(self):
        """Updates the spawn manager every frame"""
        # Every frame, tick the countdown down by 1
        self.countdown -= 1

        # If the countdown reaches 0, spawn a new obstacle
        if self.countdown <= 0:
            # Spawn a random number of obstacles
            for _ in range(randint(1, 5)):
                self.spawn_obstacle()
            # Random countdown between 50 and 100
            self.countdown = randint(25, 50)

        # Check if any obstacles have gone off the screen and remove them
        for obstacle in self._obstacles:
            if obstacle.y < -window_height() / 2 - 20:
                self.unload_obstacle(obstacle)

    def spawn_obstacle(self):
        """Spawns a new obstacle"""
        # Spawn an obstacle at a random x position and above the height of the screen
        obstacle = Obstacle(
            randint(-window_width() / 2, window_width() / 2),
            window_height() / 2 + 20,
            "red",
            "circle",
        )
        # Add to obstacle list
        self._obstacles.append(obstacle)

        # Load into collision manager
        self._collision_manager.load_obstacle(obstacle)

        # Load into game manager
        self._game_manager.load_game_object(obstacle)

    def unload_obstacle(self, target_obstacle: Obstacle):
        """Unloads an obstacle from the spawn manager

        Args:
            target_obstacle (Obstacle): Obstacle to unload
        """
        # Remove from obstacle list
        self._obstacles.remove(target_obstacle)

        # Unload from collision manager
        self._collision_manager.unload_obstacle(target_obstacle.uuid)

        # Unload from game manager
        self._game_manager.unload_game_object(target_obstacle.uuid)
