from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def copy_pic_into(small_pic, big_pic, start_x, start_y):
    for (x, y) in small_pic:
        color = small_pic.getColor(x, y)
        target_x = start_x + x
        target_y = start_y + y
        if 0 <= target_x < big_pic.getWidth() and 0 <= target_y < big_pic.getHeight():
            big_pic.setColor(target_x, target_y, color)

if __name__ == "__main__":
    green_turtle = Picture("../SampleImages/greenTurtle.jpg")
    scene = Picture("../SampleImages/bearLake.jpg")
    copy_pic_into(green_turtle, scene, 25, 25)
    copy_pic_into(green_turtle, scene, 200, 200)
    copy_pic_into(green_turtle, scene, 400, 200)
    scene.show()
    scene.save("bearLake-with-turtles.jpg")
    keep_windows_open()