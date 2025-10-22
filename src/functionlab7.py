import turtle
import math

def drawBee(turtle, centerX, centerY):
    '''stamping at the certain place'''
    turtle.up()
    turtle.goto(centerX, centerY)
    turtle.down()
    turtle.stamp()

def drawCenterCircle(turt,centerX,centerY):
    '''in the center of the flower(centerX, centerY) to draw a circle as the stamp of each flower'''
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    turt.begin_fill()
    turt.circle(15)
    turt.end_fill()
def drawFiveCircles(turt,r,x,y):
    turt.up()
    turt.goto(x, y)
    turt.down()
    for i in range(5):
        turt.begin_fill()
        turt.circle(r)
        turt.end_fill()
        turt.left(72)
def drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, centerX, centerY):
    '''draw a whole flower'''
    drawFiveCircles(sepalTurtle, 50, centerX, centerY)
    drawFiveCircles(petalTurtle, 25,  centerX, centerY)
    drawCenterCircle(centerTurtle,  centerX, centerY-15)
    drawBee(stampTurtle, centerX-2, centerY)
def drawAll():
    '''create turtle and define all parts of the flower, then click to exit'''
win = turtle.Screen()
win.bgcolor("light sky blue")
sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()


centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, 0)
drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, 220)
drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, -220)
drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, -220, 0)
drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 220, 0)

win.exitonclick()