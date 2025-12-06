from imagetools import *
from dummyWindow import keepWindowOpen
def negative(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (255 - r, 255 - g, 255 - b))
    return new_pic

if __name__ == "__main__":
    pic = getPicture("../SampleImages/mountains.jpg")
    pic.show()
    neg = negative(pic)
    neg.show()
    keepWindowOpen()