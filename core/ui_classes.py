"""Classes to be used in by the UIManager to render UI elements"""
from turtle import Turtle, _Screen
from helpers import score


class UIElement:
    """Base class for all UI elements"""

    def __init__(self, x: int, y: int, text: str, alignment: str) -> None:
        self.x = x
        self.y = y
        self.text = text
        self.alignment = alignment

    def update(self):
        """Placeholder function for UIElement update"""

    def render(self, pen: Turtle) -> None:
        """Renders the UIElement"""
        pen.goto(self.x, self.y)
        pen.color("black")
        pen.write(self.text, align=self.alignment, font=("Courier", 24, "normal"))


class ScoreUI(UIElement):
    """UIElement that displays the score"""

    def update(self):
        self.text = "Score: " + str(score.score)

    def render(self, pen: Turtle) -> None:
        """Renders the ScoreUI"""
        pen.goto(self.x, self.y)
        pen.color("black")
        pen.write(self.text, align=self.alignment, font=("Courier", 24, "normal"))


class RestartButton(UIElement):
    """UIElement that displays the restart button"""

    def __init__(self, screen: _Screen) -> None:
        super().__init__(0, -100, "Restart", "center")
        self._screen = screen
        self.width = 300
        self.height = 50
        self.font_size = 24
        self.enable_onclick()

    def update(self):
        """Placeholder function for UIElement update"""

    def render(self, pen: Turtle) -> None:
        """Renders the UIElement"""
        pen.goto(self.x, self.y)

        # Render the background fill
        pen.color("black", "white")
        pen.shape("square")
        pen.shapesize(self.height / 20, self.width / 20)
        pen.stamp()

        # Render the text
        pen.goto(self.x, self.y - 20)
        pen.color("black")
        pen.write(
            self.text, align=self.alignment, font=("Courier", self.font_size, "normal")
        )
        pen.goto(self.x, self.y)

    def enable_onclick(self):
        """Enables the restart button's onclick function"""
        self._screen.onclick(self.restart_game)

    def restart_game(self, cursor_x, cursor_y):
        """Restarts the game if the cursor is within the button's bounding box"""
        if (
            self.x - self.width / 2 < cursor_x < self.x + self.width / 2
            and self.y - self.height / 2 < cursor_y < self.y + self.height / 2
        ):
            print("Restarting game...")
