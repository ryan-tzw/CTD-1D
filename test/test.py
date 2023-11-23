"""Modules"""
import os
from turtle import Turtle, Screen, register_shape, done

print(os.getcwd())
# Register the image
register_shape("img/bulbasaur.gif")

# Create a game object with the image
game_object = Turtle()
SCREEN = Screen()
SCREEN.bgcolor("black")
game_object.shape("img/bulbasaur.gif")

# Move the game object to a specific position (optional)
game_object.penup()
game_object.goto(100, 100)
game_object.pendown()

# Additional settings if needed
# game_object.color("white")  # Set color if your image has transparency

# Example: Move the game object
game_object.forward(50)
game_object.hideturtle()
game_object.stamp()
# Keep the window open
done()
