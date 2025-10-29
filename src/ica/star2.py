import turtle
wn=turtle.Screen()
tur=turtle.Turtle()
tur.color("pink")
tur.shape("arrow")
tur.pendown()
for i in range(5):
  tur.forward(50)
  tur.right(144)

tur.penup()
tur2=turtle.Turtle()
tur2.color("pink")
tur2.shape("arrow")

tur2.penup()
tur2.goto(60,60)
tur2.pendown()
for i in range(5):
  tur2.forward(50)
  tur2.right(144)
tur2.penup()
wn.exitonclick()

