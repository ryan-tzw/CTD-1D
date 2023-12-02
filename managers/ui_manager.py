"""Manages the UI of the game"""
# pylint: disable=no-name-in-module
import logging
from turtle import Turtle, window_height, window_width, _Screen
from core.ui_classes import RestartButton, UIElement, ScoreUI


class UIManager:
    """Manages the UI of the game"""

    def __init__(self, screen: _Screen) -> None:
        self._ui_elements: list[UIElement] = []
        self.screen = screen

    def load_ui_element(self, ui_element: UIElement):
        """Adds a UIElement to the list of UIElements to be rendered

        Args:
            ui_element (UIElement): UIElement to be added
        """
        self._ui_elements.append(ui_element)

    def unload_ui_element(self, ui_element: UIElement):
        """Removes a UIElement from the list of loaded UIElements

        Args:
            target_uuid (_type_): UUID of the UIElement to remove
        """
        self._ui_elements.remove(ui_element)

        logging.warning(
            "Unable to find UIElement of UUID %s to unload.", ui_element.uuid
        )

    def update(self):
        """Updates all UIElements that have been loaded"""
        for ui_element in self._ui_elements:
            ui_element.update()

    def render(self, pen: Turtle) -> None:
        """Renders all UIElements that have been loaded"""
        for ui_element in self._ui_elements:
            ui_element.render(pen)

    def initialise_ui(self) -> None:
        """Initialises the UI"""
        score_ui = ScoreUI(
            -window_width() / 2 + 20, window_height() / 2 - 50, "Score: 0", "left"
        )
        self.load_ui_element(score_ui)

    def game_over(self, pen: Turtle) -> None:
        """Renders the game over screen"""
        self._ui_elements = []

        game_over_ui = UIElement(0, 0, "Game Over", "center")
        score_ui = ScoreUI(0, -50, "Score: 0", "center")
        restart_button = RestartButton(self.screen)

        self.load_ui_element(game_over_ui)
        self.load_ui_element(score_ui)
        self.load_ui_element(restart_button)

        self.update()
        self.render(pen)
