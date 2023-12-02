"""Main entrypoint for the game"""
# pylint: disable=no-name-in-module
from turtle import Turtle, Screen, register_shape
from core.player.player_controller import PlayerController
from core.player.player import Player
from managers.collision_manager import CollisionManager
from managers.game_manager import GameManager
from managers.input_manager import InputManager
from managers.spawn_manager import SpawnManager
from managers.ui_manager import UIManager
from helpers import delta_time, game_state


def register_shapes():
    """Registers all shapes required for the game"""
    register_shape(
        "img/bulbasaur.gif",
    )


def main():
    """Run the code from this file"""
    screen_width = 800
    screen_height = 600

    register_shapes()

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
    ui_manager = UIManager(screen)
    ui_manager.initialise_ui()

    def game_loop():
        match game_state.game_state:
            case "home_screen":
                pass

            case "playing":
                delta_time.set_start_time()
                delta_time.update_delta_time()

                # Clear screen
                pen.clear()

                game_manager.update()
                player_controller.update()
                collision_manager.update()

                spawn_manager.update()
                ui_manager.update()

                game_manager.render(pen)
                ui_manager.render(pen)

                screen.update()

                delta_time.set_end_time()
                screen.ontimer(game_loop, 10)

            case "game_over":
                ui_manager.game_over(pen)

    game_loop()

    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
