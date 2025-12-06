from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *
import math

def scale_down(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    new_w = (w + 1) // 2
    new_h = (h + 1) // 2
    new_pic = Picture(new_w, new_h)
    for x in range(new_w):
        for y in range(new_h):
            src_x = x * 2
            src_y = y * 2
            if src_x >= w: src_x = w - 1
            if src_y >= h: src_y = h - 1
            color = pic.getColor(src_x, src_y)
            new_pic.setColor(x, y, color)
    return new_pic

def scale_up(pic):
    w = pic.getWidth()
    h = pic.getHeight()
    new_w = w * 2
    new_h = h * 2
    new_pic = Picture(new_w, new_h)
    for x in range(w):
        for y in range(h):
            color = pic.getColor(x, y)
            tx = x * 2
            ty = y * 2
            if tx < new_w and ty < new_h: new_pic.setColor(tx, ty, color)
            if tx+1 < new_w and ty < new_h: new_pic.setColor(tx+1, ty, color)
            if tx < new_w and ty+1 < new_h: new_pic.setColor(tx, ty+1, color)
            if tx+1 < new_w and ty+1 < new_h: new_pic.setColor(tx+1, ty+1, color)
    return new_pic

if __name__ == "__main__":
    pic = Picture("../SampleImages/arches.jpg")
    pic.show()
    small = scale_down(pic)
    small.show()
    big = scale_up(pic)
    big.show()
    small.save("arches-scaled-down.jpg")
    big.save("arches-scaled-up.jpg")
    keep_windows_open()