#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum_weight = 0
        sum_score = 0
        for i in my_list:
            sum_score += (i[0] * i[1])
            sum_weight += i[1]
        return sum_score / sum_weight
    return 0
