from my_sum import sum3  # 假设你的函数保存在 my_sum.py 文件中

def test_sum3_ints():
    assert sum3([1, 2, 3]) == 6
    assert sum3([5, 2, 8, -2, 6, 15]) == 15
    assert sum3([-1, -2, -3, 0]) == -6
    assert sum3([0, 0, 0]) == 0

def test_sum3_floats():
    assert sum3([1.0, 2.0, 3.0]) == 6.0
    assert sum3([0.5, 0.25, 0.25]) == 1.0
    assert sum3([-1.1, 2.2, -3.3]) == -2.2