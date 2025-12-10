from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *
from random import randrange

def copy_pic_random(small_pic, big_pic):
    max_x = big_pic.getWidth() - small_pic.getWidth()
    max_y = big_pic.getHeight() - small_pic.getHeight()
    if max_x < 0 or max_y < 0:
        raise ValueError("small_pic is larger than big_pic; can't place it")
    start_x = randrange(0, max_x + 1)
    start_y = randrange(0, max_y + 1)
    for (x, y) in small_pic:
        color = small_pic.getColor(x, y)
        big_pic.setColor(start_x + x, start_y + y, color)
    return start_x, start_y
if __name__ == "__main__":
    small = Picture("../SampleImages/greenTurtle.jpg")
    big = Picture("../SampleImages/bearLake.jpg")
    for i in range(3):
        pos = copy_pic_random(small, big)
        print("Placed at", pos)
    big.show()
    big.save("bearLake-random-turtles.jpg")
    keep_windows_open()