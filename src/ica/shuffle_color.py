from imagetools import *
from dummyWindow import keepWindowOpen


def color_shuffle(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (b, r, g))
    return new_pic

if __name__ == "__main__":
    mushroom0 = Picture("../SampleImages/mushrooms.jpg")
    mushroom0.show()
    mushroom1 = color_shuffle(mushroom0)
    mushroom1.show()
    mushroom2 = color_shuffle(mushroom1)
    mushroom2.show()
    keepWindowOpen()