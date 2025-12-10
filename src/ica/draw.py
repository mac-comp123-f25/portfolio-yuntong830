from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def draw_something():
    pic = Picture(200, 200, "white")
    pic.drawOval(20, 20, 180, 180, "black", "yellow")
    pic.drawOval(70, 70, 90, 90, "black", "black")
    pic.drawOval(110, 70, 130, 90, "black", "black")
    pic.drawArc(60, 60, 140, 150, 0, 180, "arc", "black")
    return pic

def main():
    p = draw_something()
    p.show()
    keep_windows_open()

if __name__ == "__main__":
    main()