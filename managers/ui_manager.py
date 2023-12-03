"""Manages the UI of the game"""
# pylint: disable=no-name-in-module
import logging
from random import randint
from turtle import Turtle, window_height, window_width, _Screen
from core.ui_classes import (
    Button,
    NextButton,
    RestartButton,
    StartButton,
    UIElement,
    ScoreUI,
)
from helpers import score


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
        try:
            if isinstance(ui_element, Button):
                self.screen.onclick()

            self._ui_elements.remove(ui_element)
        except ValueError:
            logging.warning("Unable to find UIElement to unload.")

    def update(self):
        """Updates all UIElements that have been loaded"""
        for ui_element in self._ui_elements:
            ui_element.update()

    def render(self, pen: Turtle) -> None:
        """Renders all UIElements that have been loaded"""
        for ui_element in self._ui_elements:
            ui_element.render(pen)

    def load_home(self, pen: Turtle) -> None:
        """Renders the home screen"""
        self._ui_elements = []
        pen.clear()

        self.screen.bgpic("img/screens/home_screen.gif")

        start_button = StartButton(0, 0, self.screen)
        self.load_ui_element(start_button)

        self.update()
        self.render(pen)

    def load_loading(self, pen: Turtle) -> None:
        """Renders the loading screen"""
        self._ui_elements = []
        pen.clear()

        self.screen.bgpic("img/screens/loading_screen.gif")
        next_button = NextButton(
            window_width() / 2 - 100, window_height() / 2 - 50, self.screen
        )
        self.load_ui_element(next_button)

        self.update()
        self.render(pen)

    def load_gameplay(self) -> None:
        """Initialises the UI"""
        score_ui = ScoreUI(
            -window_width() / 2 + 20,
            window_height() / 2 - 50,
            "Score: 0",
            "black",
            "left",
        )
        self.load_ui_element(score_ui)

        # random_screen = randint(1, 5)
        # self.screen.bgpic(f"img/screens/gameplay_bg/{random_screen}.gif")

    def load_game_over(self, pen: Turtle) -> None:
        """Renders the game over screen"""
        self._ui_elements = []
        pen.clear()

        self.screen.bgpic("img/screens/game_over.gif")

        score_ui = ScoreUI(
            0,
            window_height() / 2 - 100,
            "Score: " + str(score.get_score()),
            "white",
            "center",
            48,
            "bold",
        )
        restart_button = RestartButton(
            window_width() / 2 - 200, -window_height() / 2 + 75, self.screen
        )

        self.load_ui_element(score_ui)
        self.load_ui_element(restart_button)

        self.update()
        self.render(pen)

    def reset(self):
        """Resets the UI manager"""
        self._ui_elements.clear()
