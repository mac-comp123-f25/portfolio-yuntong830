from imagetools import *
from dummyWindow import keepWindowOpen
def grayscale(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = (r + g + b) / 3
        new_pic.setColor(x, y, (lumin, lumin, lumin))
    return new_pic


def weighted_scale(pic, w1, w2, w3):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = w1 * r + w2 * g + w3 * b
        new_pic.setColor(x, y, (lumin, lumin, lumin))
    return new_pic

if __name__ == "__main__":
    pic1 = getPicture("../SampleImages/antiqueTractors.jpg")
    pic1.show()
    gray1 = grayscale(pic1)
    gray1.show()
    w_red = weighted_scale(pic1, 0.8, 0.1, 0.1)
    w_red.show()
    w_green = weighted_scale(pic1, 0.1, 0.8, 0.1)
    w_green.show()
    w_blue = weighted_scale(pic1, 0.1, 0.1, 0.8)
    w_blue.show()
    keepWindowOpen()