# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:07:55 2022

@author: sbharadwaj
"""

def read_data(filename):
    
    with open(filename) as f:
        lines = f.readlines()
        
    input_list = [int(line.strip()) for line in lines]
        
    return input_list

mass_lst = read_data("D1.txt")

# PART 1

tot_fuel = 0
for val in mass_lst:
    tot_fuel += int(val/3) - 2

print(tot_fuel)

# PART 2

tot_fuel = 0
for val in mass_lst:
    while val > 0:
        val = int(val/3) - 2
        if val > 0:
            tot_fuel += val
        
print(tot_fuel)