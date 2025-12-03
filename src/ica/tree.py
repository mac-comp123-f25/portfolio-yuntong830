import turtle
import random

def draw_fractal_tree(t, length):
    if length < 5:
        return

    t.forward(length)

    angle = random.randint(18, 32)
    weep_angle = random.randint(25, 40)

    t.left(angle)
    draw_fractal_tree(t, length * random.uniform(0.6, 0.8))

    t.right(angle + weep_angle)
    draw_fractal_tree(t, length * random.uniform(0.5, 0.7))

    t.left(weep_angle)
    t.right(angle)
    t.backward(length)


def check_draw_fractal_tree(size):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    draw_fractal_tree(t, size)
    screen.exitonclick()