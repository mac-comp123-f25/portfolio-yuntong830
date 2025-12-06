from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def rotate_left(oldPic):
    w = oldPic.getWidth()
    h = oldPic.getHeight()
    new_pic = Picture(h, w)
    for x in range(w):
        for y in range(h):
            old_color = oldPic.getColor(x, y)
            newX = y
            newY = w - x - 1
            new_pic.setColor(newX, newY, old_color)
    return new_pic

def rotate_right(oldPic):
    w = oldPic.getWidth()
    h = oldPic.getHeight()
    new_pic = Picture(h, w)
    for x in range(w):
        for y in range(h):
            color = oldPic.getColor(x, y)
            newX = h - y - 1
            newY = x
            new_pic.setColor(newX, newY, color)
    return new_pic

if __name__ == "__main__":
    pic = Picture("../SampleImages/arches.jpg")
    pic.show()
    left = rotate_left(pic)
    left.show()
    right = rotate_right(pic)
    right.show()
    left.save("arches-rotated-left.jpg")
    right.save("arches-rotated-right.jpg")
    keep_windows_open()