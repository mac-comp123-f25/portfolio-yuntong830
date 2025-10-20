def end_points(num_list):
    assert type(num_list) == list
    return (min(num_list), max(num_list))
nums = [1,4,6,8,3]
result = end_points(nums)
print(result)