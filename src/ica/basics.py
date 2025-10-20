def every_other(input_list):
    return input_list[::2]

def sum_positive(input_list):
    total = 0
    for num in input_list:
        if num > 0:
            total += num
    return total
x = ["a", "b", "c", "d"]
y = [1, 2, 3, 4]

print(every_other(x))
print(sum_positive(y))


