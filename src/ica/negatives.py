def count_negatives(First):
    if len(First) == 0:
        return 0
    else:
        first = First[0]
        rest_count=count_negatives(First[1:])
        if first <0:
            return 1+rest_count
        else:
            return rest_count
count_negatives([3,-1,4,-5,0,-1])