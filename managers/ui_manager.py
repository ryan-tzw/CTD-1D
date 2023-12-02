"""Manages the UI of the game"""
# pylint: disable=no-name-in-module
import logging
from turtle import Turtle, window_height, window_width
from helpers import score


class UIElement:
    """Base class for all UI elements"""

    def __init__(self, x: int, y: int, text: str, alignment: str) -> None:
        self.x = x
        self.y = y
        self.text = text
        self.alignment = alignment

    def update(self):
        self.text = "Score: " + str(score.score)

    def render(self, pen: Turtle) -> None:
        """Renders the UIElement"""
        pen.goto(self.x, self.y)
        pen.write(self.text, align=self.alignment, font=("Courier", 24, "normal"))


class UIManager:
    """Manages the UI of the game"""

    def __init__(self) -> None:
        self._ui_elements: list[UIElement] = []

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
        for ui_element in self._ui_elements:
            ui_element.update()

    def render(self, pen: Turtle) -> None:
        """Renders all UIElements that have been loaded"""
        for ui_element in self._ui_elements:
            ui_element.render(pen)

    def initialise_ui(self) -> None:
        """Initialises the UI"""
        score_text = "Score: " + str(score.score)
        score_ui = UIElement(
            -window_width() / 2 + 50, window_height() / 2 - 50, score_text, "left"
        )
        self.load_ui_element(score_ui)
