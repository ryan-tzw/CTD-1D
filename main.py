"""Required modules"""
from turtle import Turtle, Screen
from core.player.player_controller import PlayerController
from core.player.player import Player
from managers.collision_manager import CollisionManager
from managers.game_manager import GameManager
from managers.input_manager import InputManager
from managers.spawn_manager import SpawnManager


def main():
    """Run the code from this file"""
    screen_width = 800
    screen_height = 600

    game_manager = GameManager()

    # Initialise the Player and Screen
    pen = Turtle()
    screen = Screen()

    # Screen setup
    screen.setup(width=screen_width, height=screen_height)
    screen.title("Fablab Adventures")
    screen.tracer(0)

    # Pen setup
    pen.speed(0)
    pen.penup()
    pen.hideturtle()

    # Pass the turtle screen into the InputManager
    input_manager = InputManager()
    input_manager.set_screen(screen)
    input_manager.setup_keys()

    player = Player(0, 0, "blue", "square")
    player_controller = PlayerController(player)

    game_manager.load_game_object(player)
    collision_manager = CollisionManager(player)

    spawn_manager = SpawnManager(game_manager, collision_manager)

    def game_loop():
        # Clear screen
        pen.clear()

        game_manager.update()
        player_controller.update()
        collision_manager.update()

        spawn_manager.update()

        game_manager.render(pen)

        screen.update()
        screen.ontimer(game_loop, 10)

    game_loop()

    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
