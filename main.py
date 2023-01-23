from turtle import Turtle, Screen

tanya = Turtle()
screen = Screen()


def move_forwards():
    tanya.forward(10)


def move_backwards():
    tanya.backward(10)


def turn_right():
    tanya.right(10)


def turn_left():
    tanya.left(10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="c", fun=screen.resetscreen)
screen.exitonclick()
