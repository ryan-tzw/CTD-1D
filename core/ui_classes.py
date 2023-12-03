"""Classes to be used in by the UIManager to render UI elements"""
from turtle import Turtle, _Screen
from helpers import score, game_state


class UIElement:
    """Base class for all UI elements"""

    def __init__(
        self, x: int = 0, y: int = 0, text: str = "Placeholder", alignment: str = "left"
    ) -> None:
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

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        text: str = "Placeholder",
        text_color: str = "white",
        alignment: str = "left",
        font_size: int = 24,
        font_type: str = "normal",
    ) -> None:
        super().__init__(x, y, text, alignment)
        self.text_color = text_color
        self.font_size = font_size
        self.font_type = font_type

    def update(self):
        self.text = "Score: " + str(score.get_score())

    def render(self, pen: Turtle) -> None:
        """Renders the ScoreUI"""
        pen.goto(self.x, self.y)
        pen.color(self.text_color)
        pen.write(
            self.text,
            align=self.alignment,
            font=("Courier", self.font_size, self.font_type),
        )


class Button(UIElement):
    """Base class for all buttons"""

    def __init__(
        self,
        x: int,
        y: int,
        screen: _Screen,
        width: int = 50,
        height: int = 50,
        font_size: int = 24,
        font_type: str = "normal",
        bg_color: str = "white",
        border_color: str = "black",
        text_color: str = "black",
        text: str = "Placeholder",
        alignment: str = "center",
    ) -> None:
        super().__init__(x, y, text, alignment)
        self._screen = screen
        self.width = width
        self.height = height
        self.font_size = font_size
        self.font_type = font_type
        self.bg_color = bg_color
        self.border_color = border_color
        self.text_color = text_color

        self.enable_onclick()

    def render(self, pen: Turtle) -> None:
        """Renders the UIElement"""
        # Render the background fill
        pen.goto(self.x, self.y)
        pen.color(self.border_color, self.bg_color)
        pen.shape("square")
        pen.shapesize(self.height / 20, self.width / 20)
        pen.stamp()

        # Render the text
        pen.goto(self.x, self.y - 20)
        pen.color(self.text_color)
        pen.write(
            self.text,
            align=self.alignment,
            font=("Courier", self.font_size, self.font_type),
        )
        pen.goto(self.x, self.y)

    def enable_onclick(self):
        """Enables the button's onclick function"""
        self._screen.onclick(self.on_click)

    def on_click(self, cursor_x, cursor_y):
        """Checks if the cursor is within the button's bounding box"""
        if (
            self.x - self.width / 2 < cursor_x < self.x + self.width / 2
            and self.y - self.height / 2 < cursor_y < self.y + self.height / 2
        ):
            self.on_click_handler()

    def on_click_handler(self):
        """Placeholder function for button functionality"""


class StartButton(Button):
    """UIElement that displays the start button"""

    def __init__(self, x: int, y: int, screen: _Screen) -> None:
        super().__init__(
            x, y, screen, text="Start", bg_color="#f8efc0", font_type="bold"
        )
        self.width = 300
        self.height = 50
        self.font_size = 24
        self.enable_onclick()

    def on_click_handler(self):
        """Starts the game if the cursor is within the button's bounding box"""
        game_state.set_game_state("loading")


class NextButton(Button):
    """UIElement that displays the next button"""

    def __init__(
        self,
        x: int,
        y: int,
        screen: _Screen,
    ) -> None:
        super().__init__(x, y, screen, 150, 50, text="Next", bg_color="#f8efc0")

    def on_click_handler(self):
        """Loads the next level if the cursor is within the button's bounding box"""
        game_state.set_game_state("starting")


class RestartButton(Button):
    """UIElement that displays the restart button"""

    def __init__(self, x, y, screen: _Screen) -> None:
        super().__init__(
            x,
            y,
            screen,
            text="Restart?",
            alignment="center",
        )
        self.width = 300
        self.height = 50
        self.font_size = 24
        self.enable_onclick()

    def render(self, pen: Turtle) -> None:
        """Renders the UIElement"""
        pen.goto(self.x, self.y)

        # Render the background fill
        pen.color("black", "#3aa2a8")
        pen.shape("square")
        pen.shapesize(self.height / 20, self.width / 20)
        pen.stamp()

        # Render the text
        pen.goto(self.x, self.y - 20)
        pen.color("white")
        pen.write(
            self.text, align=self.alignment, font=("Courier", self.font_size, "bold")
        )
        pen.goto(self.x, self.y)

    def on_click_handler(self):
        """Restarts the game if the cursor is within the button's bounding box"""
        game_state.set_game_state("starting")
