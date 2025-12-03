import turtle
def calc_next_size(size):
    return size / (2 ** 0.5)


def draw_levy(turt, size, reps):

    if reps == 1:
        turt.forward(size)
        return

    new_size = calc_next_size(size)

    turt.left(45)
    draw_levy(turt, new_size, reps - 1)

    turt.right(90)
    draw_levy(turt, new_size, reps - 1)

    turt.left(45)

def check_draw_levy(size, reps):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed("fastest")

    draw_levy(t, size, reps)
    screen.exitonclick()