from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def main():
    pic = Picture("../SampleImages/mightyMidway.jpg")
    width = pic.getWidth()
    height = pic.getHeight()
    print("Number of pixels:", width * height)
    copy_pic = pic.copy()
    red = (255, 0, 0)
    copy_pic.setColor(0, 0, red)
    copy_pic.setColor(width - 1, 0, red)
    copy_pic.setColor(0, height - 1, red)
    copy_pic.setColor(width - 1, height - 1, red)
    copy_pic.save("mightyMidway-redCorners.jpg")
    copy_pic.explore()

    keep_windows_open()

if __name__ == "__main__":
    main()