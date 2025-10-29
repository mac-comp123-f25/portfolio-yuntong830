import turtle
import math

def draw_nested_squares(turt):
    for i in range(10,81,10):
        for j in range(4):
            turt.forward(i)
            turt.left(90)

win=turtle.Screen()
tt=turtle.Turtle()
draw_nested_squares(tt)
win.exitonclick()