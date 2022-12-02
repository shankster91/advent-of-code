# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 12:16:01 2022

@author: sbharadwaj
"""

def read_data(filename):
    
    with open(filename) as f:
        lines = f.readlines()
        
    input_list = [line.strip() for line in lines]
        
    return input_list

game_lst = read_data("D2.txt")

# PART 1

tot_score = 0
for pair in game_lst:
    pair = pair.split()
    if pair[0] == 'A':
        if pair[1] == 'X':
            tot_score += 4
        elif pair[1] == 'Y':
            tot_score += 8
        else:
            tot_score += 3
    elif pair[0] == 'B':
        if pair[1] == 'X':
            tot_score += 1
        elif pair[1] == 'Y':
            tot_score += 5
        else:
            tot_score += 9
    else:
        if pair[1] == 'X':
            tot_score += 7
        elif pair[1] == 'Y':
            tot_score += 2
        else:
            tot_score += 6
            
print(tot_score)

# PART 2

tot_score = 0
for pair in game_lst:
    pair = pair.split()
    if pair[0] == 'A':
        if pair[1] == 'X':
            tot_score += 3
        elif pair[1] == 'Y':
            tot_score += 4
        else:
            tot_score += 8
    elif pair[0] == 'B':
        if pair[1] == 'X':
            tot_score += 1
        elif pair[1] == 'Y':
            tot_score += 5
        else:
            tot_score += 9
    else:
        if pair[1] == 'X':
            tot_score += 2
        elif pair[1] == 'Y':
            tot_score += 6
        else:
            tot_score += 7
            
print(tot_score)
