def sum3(values):
    assert type(values) in [list, tuple]
    assert len(values) >= 3
    assert all(type(values[i]) in [int, float] for i in range(3))
    total=values[0] + values[1] + values[2]
    return total

if __name__ == "__main__":
  print( sum3([5, 2, 8, -2, 6, 15]) )
  #print( sum3([5, 2]) )
  #print( sum3(5) )
  #print( sum3(["h", "i", 1, 2, 3]) )
  print( sum3([1, 2, 3, "h", "i"]) )

