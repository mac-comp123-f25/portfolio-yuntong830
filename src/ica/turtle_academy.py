import turtle
wn=turtle.Screen()
turt=turtle.Turtle()
turt.color("green")
turt.begin_fill()
for i in range(6):
    turt.forward(100)
    turt.left(60)
    turt.forward(100)
    turt.right(120)
turt.end_fill()
turtle.exitonclick()