from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def crop_picture(pic, start_x, start_y, crop_w, crop_h):
    crop_w = int(crop_w)
    crop_h = int(crop_h)

    new_pic = Picture(crop_w, crop_h)
    for x in range(crop_w):
        for y in range(crop_h):
            src_x = start_x + x
            src_y = start_y + y
            if 0 <= src_x < pic.getWidth() and 0 <= src_y < pic.getHeight():
                color = pic.getColor(src_x, src_y)
            else:
                color = (0, 0, 0)
            new_pic.setColor(x, y, color)
    return new_pic

if __name__ == "__main__":
    dam = Picture("../SampleImages/hooverDam.jpg")
    dam_crop1 = crop_picture(dam, 260, 90, 240, 210)
    dam_crop2 = crop_picture(dam, 100, 150, 100, 150)
    dam.show()
    dam_crop1.show()
    dam_crop2.show()
    dam_crop1.save("hooverDam-crop1.jpg")
    dam_crop2.save("hooverDam-crop2.jpg")
    keep_windows_open()