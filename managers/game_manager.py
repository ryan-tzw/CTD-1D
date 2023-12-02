"""Manages the updating & rendering of all game objects"""
import logging
from core.generics import GameObject


class GameManager:
    """Manages the updating & rendering of all game objects"""

    def __init__(self) -> None:
        self._game_objects: list[GameObject] = []

    def load_game_object(self, game_object: GameObject):
        """Adds a GameObject to the list of GameObjects to be rendered

        Args:
            game_object (GameObject): GameObject to be added
        """
        self._game_objects.append(game_object)
        self._game_objects.sort(key=lambda obj: obj.render_priority)

    def unload_game_object(self, game_object: GameObject):
        """Removes a GameObject from the list of loaded GameObjects

        Args:
            target_uuid (_type_): UUID of the GameObject to remove
        """
        try:
            self._game_objects.remove(game_object)
        except ValueError:
            logging.warning("Unable to find GameObject to unload.")

    def update(self):
        """Updates all GameObjects that have been loaded"""
        for game_object in self._game_objects:
            game_object.update()

    def render(self, pen):
        """Renders all GameObjects that have been loaded"""
        for game_object in self._game_objects:
            game_object.render(pen)

    def reset(self):
        """Resets the game manager"""
        self._game_objects.clear()
