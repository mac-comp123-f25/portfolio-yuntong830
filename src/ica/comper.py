def times_n(number, list_of_numbers):
    return [x*number for x in list_of_numbers]
nums = [1, 2, 3, 2, 4]
result = times_n(3, nums)
print(times_n(3, nums))

def remove_all_comp(value, list):
    return [x for x in list if x != value]
nums = [1, 2, 3, 2, 4, 2]
print(remove_all_comp(2, nums))