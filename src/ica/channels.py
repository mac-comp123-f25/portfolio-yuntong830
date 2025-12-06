from imagetools import *
from dummyWindow import keepWindowOpen
def red_channel(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (r, 0, 0))
    return new_pic

def green_channel(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (0, g, 0))
    return new_pic

def blue_channel(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (0, 0, b))
    return new_pic

if __name__ == "__main__":
    pic = Picture("../SampleImages/astilbe.jpg")
    pic.show()
    r_img = red_channel(pic)
    g_img = green_channel(pic)
    b_img = blue_channel(pic)
    r_img.show()
    g_img.show()
    b_img.show()
    keepWindowOpen()