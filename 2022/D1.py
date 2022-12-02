# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:29:40 2022

@author: shank
"""

def read_data(filename):
    
    with open(filename) as f:
        lines = f.readlines()
        
    input_list = [line.strip() for line in lines]
        
    return input_list

cal_lst = read_data("D1.txt")

cal_sum = 0
sum_lst = []

for val in cal_lst:
    if val == '':
        sum_lst.append(cal_sum)
        cal_sum = 0
    else:
        cal_sum += int(val)
        
sum_lst.sort()
print(sum_lst[-1])
print(sum_lst[-1] + sum_lst[-2] + sum_lst[-3])