# pylint: disable=no-name-in-module
"""Required modules"""
import os
from turtle import Turtle, Screen, done, register_shape

print(os.getcwd())

game_object = Turtle()
SCREEN = Screen()
SCREEN.bgcolor("black")

register_shape("img/bulbasaur.gif")

game_object.shape("img/bulbasaur.gif")

game_object.hideturtle()
game_object.stamp()
# Keep the window open
done()
