import turtle
def spiral_in(turt, side_len):
    if side_len <5:
        return
    turt.forward(side_len)
    turt.right(90)
    spiral_in(turt, side_len-5)
def check_spiral_in(start_len):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    spiral_in(t, start_len)
    screen.mainloop()
check_spiral_in(200)