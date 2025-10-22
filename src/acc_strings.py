def copy_str(string, num_times):
    ans_str =  ""    # initialize accumulator to empty string
    for x in range(num_times):
        ans_str = ans_str + string     # update ans_str
        print("After iteration", x + 1, ":", ans_str)
    return ans_str
stat = copy_str("hello", 3)
print(stat)

