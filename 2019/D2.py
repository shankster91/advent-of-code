# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:01:01 2022

@author: sbharadwaj
"""

def read_data(filename):
    
    with open(filename) as f:
        lines = f.readlines()
        
    input_list = [line.strip() for line in lines]
        
    return input_list

op_lst = read_data("D2.txt")[0].split(',')
op_lst[1] = '79'
op_lst[2] = '12'

i = 0

while int(op_lst[i]) != 99:
    p1 = int(op_lst[i+1])
    p2 = int(op_lst[i+2])
    p3 = int(op_lst[i+3])
    if int(op_lst[i]) == 1:
        op_lst[p3] = int(op_lst[p1]) + int(op_lst[p2])
    elif int(op_lst[i]) == 2:
            op_lst[p3] = int(op_lst[p1]) * int(op_lst[p2])
    i += 4
    
print(op_lst)
    
    