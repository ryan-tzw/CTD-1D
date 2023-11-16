from turtle import Turtle, Screen

speed = 0
direction = 0


def move_right():
    player.setheading(0)
    start_move()


def move_up():
    player.setheading(90)
    start_move()


def move_left():
    player.setheading(180)
    start_move()


def move_down():
    player.setheading(270)
    start_move()


def start_move():
    global speed
    speed = 10


def end_move():
    global speed
    speed = 0


def move():
    player.forward(speed)


player = Turtle()
screen = Screen()

screen.title("Test")
screen.tracer(0)
player.penup()

screen.onkeypress(move_right, "d")
screen.onkeypress(move_up, "w")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_down, "s")

screen.onkeyrelease(end_move, "d")
screen.onkeyrelease(end_move, "w")
screen.onkeyrelease(end_move, "a")
screen.onkeyrelease(end_move, "s")


def game_loop():
    move()
    screen.update()
    screen.ontimer(game_loop, 50)


game_loop()

screen.listen()
screen.mainloop()
