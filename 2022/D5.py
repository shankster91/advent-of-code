# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:07:20 2022

@author: sbharadwaj
"""
import re

def read_data(filename):
    
    with open(filename) as f:
        lines = f.readlines()
        
    input_lst = [line.strip('\n') for line in lines if line[0] != 'm']
    input_lst = input_lst[:len(input_lst) - 2]
    dir_lst = [line.strip('\n') for line in lines if line[0] == 'm']
        
    return input_lst, dir_lst

inp_lst, dir_lst = read_data("D5.txt")


stack_dict = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [],
              8: [], 9: []}

for row in inp_lst:
    idx = 1
    box = 1
    while idx < len(row):
        if row[idx] != ' ':
            stack_dict[box] += [row[idx]]
        idx += 4
        box += 1
        
for dir_str in dir_lst:
    nums = re.findall('[0-9]+', dir_str)
    move_num, from_box, to_box = int(nums[0]), int(nums[1]), int(nums[2])
    move_lst = stack_dict[from_box][:move_num]
    stack_dict[from_box] = stack_dict[from_box][move_num:]
    #move_lst.reverse() # Diff between Part 1 and Part 2
    stack_dict[to_box] = move_lst + stack_dict[to_box]

fin_str = ''
for i in range(1,10):
    fin_str += stack_dict[i][0]
    
print(fin_str)
    
