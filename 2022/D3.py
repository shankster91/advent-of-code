# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:31:45 2022

@author: sbharadwaj
"""

def read_data(filename):
    
    with open(filename) as f:
        lines = f.readlines()
        
    input_list = [line.strip() for line in lines]
        
    return input_list


comp_lst = read_data("D3.txt")

# PART 1

tot_sum = 0
for comp in comp_lst:
    mid = len(comp)//2
    s1 = set(comp[:mid])
    s2 = set(comp[mid:])
    intsec = s1.intersection(s2).pop()

    if intsec.isupper():
        tot_sum += ord(intsec) - 38
    else:
        tot_sum += ord(intsec) - 96
        
print(tot_sum)

# PART 2

tot_sum = 0
i = 0
while i < len(comp_lst):
    comps = comp_lst[i:i+3]
    s1 = set(comps[0])
    s2 = set(comps[1])
    s3 = set(comps[2])
    intsec = s1.intersection(s2).intersection(s3).pop()

    if intsec.isupper():
        tot_sum += ord(intsec) - 38
    else:
        tot_sum += ord(intsec) - 96
    i += 3
        
print(tot_sum)