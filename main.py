from turtle import Turtle, Screen
from classes.managers.input_manager import InputManager

# Initial setup
player = Turtle()
screen = Screen()

screen.title("Wow game")
screen.tracer(0)
player.penup()

input_manager = InputManager(player, screen)
input_manager.setup_keys()


def game_loop():
    input_manager.move()
    screen.update()
    screen.ontimer(game_loop, 50)


game_loop()

screen.listen()
screen.mainloop()
