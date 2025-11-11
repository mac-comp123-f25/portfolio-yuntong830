import math

def rect_area(wid, len):
    x=wid*len
    return x

def roof_cost(area, sqf_cost):
    y=area*sqf_cost
    return y
def estimate_green_roof(wid, len, sqf_cost):
    area = rect_area(wid, len)
    cost = roof_cost(area, sqf_cost)
    return(area,cost)
area,cost=estimate_green_roof(33,55,35)
print("area=",area)
print("cost=$",cost)