import turtle
wn=turtle.Screen()
turt=turtle.Turtle()
turt.shape("arrow")
turt.color("green")
turt.begin_fill()
for i in range(3):
    turt.forward(100)
    turt.left(120)
turt.end_fill()
wn.exitonclick()
