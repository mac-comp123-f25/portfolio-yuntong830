def smallest_diff(x, y, z):
    diff1 = abs(x - y)
    diff2 = abs(y - z)
    diff3 = abs(x - z)
    min_diff = min(diff1, diff2, diff3)
    return min_diff
print(smallest_diff(32,43,90))
'''
Local environmen
   x    32
   y    43
   z    90
   diff1    11
   diff2    47
   diff3    58
   min_diff    11

Reture 11
'''