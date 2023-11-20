"""Required modules"""
from turtle import Turtle, Screen
from classes.managers.input_manager import InputManager


def main():
    """Run the code from this file"""
    screen_width = 800
    screen_height = 600

    # Initialise the Player and Screen
    player = Turtle()
    screen = Screen()

    # Screen setup
    screen.setup(width=screen_width, height=screen_height)
    screen.title("Wow game")
    screen.tracer(0)

    # Player setup
    player.penup()
    player.shape("turtle")
    player.color("green")

    # Instantiate the InputManager
    input_manager = InputManager(player, screen)

    def game_loop():
        input_manager.move()
        screen.update()
        screen.ontimer(game_loop, 20)

    game_loop()

    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
