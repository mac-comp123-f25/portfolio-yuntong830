import math
def sum_range(start_val, end_val):
    cnt=0
    for x in range(start_val, end_val+1):
        cnt=cnt+x
    return cnt
straightforward=sum_range(1,5)
print(straightforward)
passednumber=sum_range(8,8)
print(passednumber)
greater=sum_range(8,6)
print(greater)
negative=sum_range(-7,-5)
print(negative)