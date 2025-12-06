from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def simple_blend(p1, p2):
    w = p1.getWidth()
    h = p1.getHeight()
    new_pic = Picture(w, h)
    for (x, y) in new_pic:
        r1, g1, b1 = p1.getColor(x, y)
        r2, g2, b2 = p2.getColor(x, y)
        new_r = int(round((r1 + r2) / 2.0))
        new_g = int(round((g1 + g2) / 2.0))
        new_b = int(round((b1 + b2) / 2.0))
        new_pic.setColor(x, y, (new_r, new_g, new_b))
    return new_pic

def blend2(p1, p2):
    w = min(p1.getWidth(), p2.getWidth())
    h = min(p1.getHeight(), p2.getHeight())
    new_pic = Picture(w, h)
    for x in range(w):
        for y in range(h):
            r1, g1, b1 = p1.getColor(x, y)
            r2, g2, b2 = p2.getColor(x, y)
            new_r = int(round((r1 + r2) / 2.0))
            new_g = int(round((g1 + g2) / 2.0))
            new_b = int(round((b1 + b2) / 2.0))
            new_pic.setColor(x, y, (new_r, new_g, new_b))
    return new_pic

def weighted_blend(p1, p2, wgt1):
    wgt2 = 1.0 - wgt1
    w = min(p1.getWidth(), p2.getWidth())
    h = min(p1.getHeight(), p2.getHeight())
    new_pic = Picture(w, h)
    for x in range(w):
        for y in range(h):
            r1, g1, b1 = p1.getColor(x, y)
            r2, g2, b2 = p2.getColor(x, y)
            new_r = int(round(wgt1 * r1 + wgt2 * r2))
            new_g = int(round(wgt1 * g1 + wgt2 * g2))
            new_b = int(round(wgt1 * b1 + wgt2 * b2))
            new_pic.setColor(x, y, (new_r, new_g, new_b))
    return new_pic

if __name__ == "__main__":
    p1 = Picture("../SampleImages/daylilies.jpg")
    p2 = Picture("../SampleImages/wildColumbine.jpg")
    p1.show()
    p2.show()
    p3 = simple_blend(p1, p2)
    p3.show()
    p4 = Picture("../SampleImages/muirWoods.jpg")
    p5 = Picture("../SampleImages/peony.jpg")
    pb = blend2(p4, p5)
    pb.show()
    pw = weighted_blend(p4, p5, 0.25)
    pw.show()
    keep_windows_open()