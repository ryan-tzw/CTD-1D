"""Main entrypoint for the game"""
# pylint: disable=no-name-in-module
import os
from turtle import Turtle, Screen, register_shape
from core.player.player_controller import PlayerController
from core.player.player import Player
from managers.collision_manager import CollisionManager
from managers.game_manager import GameManager
from managers.input_manager import InputManager
from managers.spawn_manager import SpawnManager
from managers.ui_manager import UIManager
from helpers import delta_time, game_state, score, difficulty


def register_shapes():
    """Registers all shapes required for the game"""
    for dirpath, _, filenames in os.walk("img"):
        for filename in [f for f in filenames if f.endswith(".gif")]:
            shape_to_register = os.path.join(dirpath, filename).replace("\\", "/")
            register_shape(shape_to_register)
            print("Registered shape: " + shape_to_register)


def main():
    """Run the code from this file"""
    screen_width = 1024
    screen_height = 768

    register_shapes()

    game_manager = GameManager()

    # Initialise the Player and Screen
    pen = Turtle()
    screen = Screen()

    # Pen setup
    pen.speed(0)
    pen.penup()
    pen.hideturtle()

    # Screen setup
    screen.setup(width=screen_width, height=screen_height)
    screen.title("Fablab Adventures")
    screen.tracer(0)
    # pylint: disable=protected-access
    screen.cv._rootwindow.resizable(False, False)

    # Pass the turtle screen into the InputManager
    input_manager = InputManager()
    input_manager.set_screen(screen)
    input_manager.setup_keys()

    player = Player(0, 0, "blue", "img/player.gif")
    player_controller = PlayerController(player)

    game_manager.load_game_object(player)
    collision_manager = CollisionManager(player)

    spawn_manager = SpawnManager(game_manager, collision_manager)
    ui_manager = UIManager(screen)
    ui_manager.load_gameplay()

    def game_loop():
        match game_state.get_game_state():
            case "home_screen":
                ui_manager.load_home(pen)

            case "loading":
                ui_manager.load_loading(pen)

            case "starting":
                screen.bgpic("nopic")
                difficulty.reset()
                player.reset_position()
                score.reset_score()
                spawn_manager.reset()
                ui_manager.reset()
                ui_manager.load_gameplay()
                game_state.set_game_state("playing")

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

            case "game_over":
                ui_manager.load_game_over(pen)

        screen.ontimer(game_loop, 10)

    game_loop()

    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
