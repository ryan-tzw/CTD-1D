"""Required modules"""
import logging
from uuid import UUID
from core.generics import GameObject
from core.player.player import Player
from helpers.vector import Vector


class CollisionManager:
    """Checks for collision between Player and all other GameObjects

    Returns:
        _type_: _description_
    """

    def __init__(self, player: Player) -> None:
        self._obstacles: list[GameObject] = []
        self._player = player

    def global_check(self):
        for obstacle in self._obstacles:
            if self._collision_check(self._player, obstacle):
                collision_direction = self._find_collision_direction(
                    self._player, obstacle
                )

                match collision_direction:
                    case "above":
                        self._player.dy += 1 * self._player.move_speed
                    case "below":
                        self._player.dy -= 1 * self._player.move_speed
                    case "left":
                        self._player.dx -= 1 * self._player.move_speed
                    case "right":
                        self._player.dx += 1 * self._player.move_speed

    def _collision_check(self, object1: GameObject, object2: GameObject):
        """Checks for collision using axis-aligned bounding boxes"""
        bb1 = object1.boundingbox
        bb2 = object2.boundingbox
        if (
            bb1.min_x <= bb2.max_x
            and bb1.max_x >= bb2.min_x
            and bb1.min_y <= bb2.max_y
            and bb1.max_y >= bb2.min_y
        ):
            return True
        return False

    def _find_collision_direction(self, object1: GameObject, object2: GameObject):
        displacement = Vector(object1.x, object1.y)
        displacement.subtract(Vector(object2.x, object2.y))
        rotation = displacement.get_rotation()
        print(rotation)

        if 45 <= rotation < 135:
            return "above"
        elif 135 <= rotation < 225:
            return "left"
        elif 225 <= rotation < 315:
            return "below"
        else:
            return "right"

    def load_obstacle(self, obstacle: GameObject):
        self._obstacles.append(obstacle)

    def unload_obstacle(self, target_uuid: UUID):
        for obstacle in self._obstacles:
            if obstacle.uuid == target_uuid:
                self._obstacles.remove(obstacle)
                return
        logging.warning("Unable to find obstacle %s to unregister.", target_uuid)

    def update(self):
        self.global_check()
