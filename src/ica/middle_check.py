def middle_value(x,y,z):
    if x >= y:
        if x <= z:
            return x
        else:
            if y >= z:
                return y
            else:
                return z
    else:  # x < y
        if x >= z:
            return x
        else:
            if y <= z:
                return y
            else:
                return z
if __name__ == "__main__":
        assert middle_value(5, 2, 77) == 5
        assert middle_value(-10, 50, 57) == 50
        assert middle_value(-1, -6, -3) == -3
        print("All tests passed!")
