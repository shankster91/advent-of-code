# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:20:48 2022

@author: sbharadwaj
"""

def read_data(filename):
    
    with open(filename) as f:
        lines = f.readlines()
        
    input_list = [line.strip() for line in lines]
        
    return input_list

inst_lst = read_data("D4.txt")

count_p1 = 0
count_p2 = 0
for pair in inst_lst:
    first, second = pair.split(",")
    first_l, first_h = first.split("-")
    second_l, second_h = second.split("-")
    first_set = set(range(int(first_l), int(first_h) + 1))
    second_set = set(range(int(second_l), int(second_h) + 1))
    if (first_set <= second_set or second_set <= first_set):
        count_p1 += 1
    if len(first_set.intersection(second_set)) > 0:
        count_p2 += 1
        
print(count_p1)
print(count_p2)