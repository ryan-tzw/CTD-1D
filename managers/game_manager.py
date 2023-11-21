"""Required modules"""
import logging
from uuid import UUID
from core.generics import GameObject


class GameManager:
    """Manages the updating & rendering of all game objects"""

    def __init__(self) -> None:
        self._game_objects = []

    def load_game_object(self, game_object: GameObject):
        """Adds a GameObject to the list of GameObjects to be rendered

        Args:
            game_object (GameObject): GameObject to be added
        """
        self._game_objects.append(game_object)

    def unload_game_object(self, target_uuid: UUID):
        """Removes a GameObject from the list of loaded GameObjects

        Args:
            target_uuid (_type_): UUID of the GameObject to remove
        """
        for game_object in self._game_objects:
            if game_object.uuid == target_uuid:
                self._game_objects.remove(game_object)
            else:
                logging.warning(
                    "Unable to find GameObject of UUID %s to unload.", target_uuid
                )

    def update(self):
        """Updates all GameObjects that have been loaded"""
        for game_object in self._game_objects:
            game_object.update()

    def render(self, pen):
        """Renders all GameObjects that have been loaded"""
        for game_object in self._game_objects:
            game_object.render(pen)
