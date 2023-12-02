"""A module containing the SpawnManager class"""
# pylint: disable=no-name-in-module
from random import randint
from turtle import window_height, window_width
from core.generics import Obstacle
from managers.collision_manager import CollisionManager
from managers.game_manager import GameManager
from helpers import score, difficulty


class SpawnManager:
    """Spawns falling obstacles"""

    def __init__(
        self, game_manager: GameManager, collision_manager: CollisionManager
    ) -> None:
        self._game_manager = game_manager
        self._collision_manager = collision_manager
        self._obstacles: list[Obstacle] = []
        self.countdown = 75

    def update(self):
        """Updates the spawn manager every frame"""
        # Every frame, tick the countdown down by 1
        self.countdown -= 1

        # If the countdown reaches 0, spawn a new obstacle
        if self.countdown <= 0:
            # Spawn a random number of obstacles
            for _ in range(randint(1, 5)):
                self.spawn_obstacle()

            self.countdown = randint(20, 40) / difficulty.get_global_speed_modifier()

        # Check if any obstacles have gone off the screen and remove them
        for obstacle in self._obstacles:
            if obstacle.y < -window_height() / 2 - obstacle.height:
                self.unload_obstacle(obstacle)
                score.add_score()

    def spawn_obstacle(self):
        """Spawns a new obstacle"""
        # Spawn an obstacle at a random x position and above the height of the screen
        obstacle = Obstacle(
            randint(-window_width() / 2, window_width() / 2),
            window_height() / 2 + 20,
            "red",
        )

        self._obstacles.append(obstacle)
        self._collision_manager.load_obstacle(obstacle)
        self._game_manager.load_game_object(obstacle)

    def unload_obstacle(self, target_obstacle: Obstacle):
        """Unloads an obstacle from the spawn manager

        Args:
            target_obstacle (Obstacle): Obstacle to unload
        """
        self._obstacles.remove(target_obstacle)
        self._collision_manager.unload_obstacle(target_obstacle)
        self._game_manager.unload_game_object(target_obstacle)

    def reset(self):
        """Resets the spawn manager"""
        # Unload all obstacles
        for obstacle in self._obstacles:
            self.unload_obstacle(obstacle)
        # Reset countdown
        self.countdown = 75
