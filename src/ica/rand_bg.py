from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *
from random import randrange

def get_rand_bg():
    r = randrange(0, 256)
    g = randrange(0, 256)
    b = randrange(0, 256)
    pic = Picture(100, 100)
    pic.setAllPixels((r, g, b))
    return pic

def main():
    p = get_rand_bg()
    p.show()
    keep_windows_open()

if __name__ == "__main__":
    main()