def string_of_nums(x):
    ans_str=''
    for i in range(1,x+1):
        ans_str=ans_str+str(i)
        if i<x:
            ans_str = ans_str + " "
    return ans_str
stat=string_of_nums(8)
print(stat)