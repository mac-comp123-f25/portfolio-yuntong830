import turtle
from selectors import SelectSelector


def tele_turtle(n):
  win = turtle.Screen()
  tele_t = turtle.Turtle()
  for i in range(n):
    move = input("Enter next move:f")
    do_move(tele_t, move)
  win.exitonclick()

def do_move(turt, move):
    if move =='r':
        turt.right(90)
    elif move =='f':
        turt.forward(15)
    elif move == 'l':
        turt.left(90)
    elif move == 'b':
        turt.backward(15)
    else:
        print('invalid move')
if __name__ == "__main__":
        tele_turtle(10)  # will ask the user to enter 10 commands, use other
        # values and notice what will happen


