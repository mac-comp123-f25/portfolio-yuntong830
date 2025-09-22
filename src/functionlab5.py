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
drawFiveCircles(sepalTurtle, 50, 0, 0)
drawFiveCircles(petalTurtle, 25, 0, 0)
drawFiveCircles(sepalTurtle, 50, 0, 220)
drawFiveCircles(petalTurtle, 25, 0, 220)
drawFiveCircles(sepalTurtle, 50, 0, -220)
drawFiveCircles(petalTurtle, 25, 0, -220)
drawFiveCircles(sepalTurtle, 50, -220, 0)
drawFiveCircles(petalTurtle, 25, -220, 0)
drawFiveCircles(sepalTurtle, 50, 220, 0)
drawFiveCircles(petalTurtle, 25, 220, 0)

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

drawCenterCircle(centerTurtle,  0, -15)
drawCenterCircle(centerTurtle,0, 205)
drawCenterCircle(centerTurtle, 220, -15)
drawCenterCircle(centerTurtle, -220, -15)
drawCenterCircle(centerTurtle, 0, -235)

drawBee(stampTurtle,-2, 0)
drawBee(stampTurtle,-2, 220)
drawBee(stampTurtle,218, 0)
drawBee(stampTurtle,-2, -220)
drawBee(stampTurtle,-222, 0)
win.exitonclick()