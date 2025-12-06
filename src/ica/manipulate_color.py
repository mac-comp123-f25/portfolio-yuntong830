from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def change_red(picture, factor):
    for (x, y) in picture:
        (r, g, b) = picture.getColor(x, y)
        picture.setColor(x, y, (r * factor, g, b))

def change_blue(picture, factor):
    for (x, y) in picture:
        (r, g, b) = picture.getColor(x, y)
        picture.setColor(x, y, (r, g, b * factor))

def remove_blue(picture):
    for (x, y) in picture:
        (r, g, b) = picture.getColor(x, y)
        picture.setColor(x, y, (r, g, 0))

def fix_green(picture, value):
    for (x, y) in picture:
        (r, g, b) = picture.getColor(x, y)
        picture.setColor(x, y, (r, value, b))

def main():
    pic = Picture("../SampleImages/raspberries.jpg")
    pic.show()
    change_blue(pic, 2)
    pic.show()
    keep_windows_open()

if __name__ == "__main__":
    main()