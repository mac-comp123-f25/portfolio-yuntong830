import turtle
wn=turtle.Screen()
turt=turtle.Turtle()
n=8
turt.shape("arrow")
turt.color("green")
turt.begin_fill()
for i in range(n):
    turt.forward(100)
    turt.left(360/n)
turt.end_fill()
wn.exitonclick()
