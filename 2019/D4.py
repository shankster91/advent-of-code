# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 20:21:57 2022

@author: sbharadwaj
"""

def case1_check(num):
    
    str_num = str(num)
    for i in range(5):
        if str_num[i] == str_num[i+1]:
            return True
    
    return False

def case1_p2_check(num):
    
    str_num = str(num)
    repeat_digit_cnt = []
    cnt = 1
    for i in range(5):
        if str_num[i] == str_num[i+1]:
            cnt += 1
        else:
            repeat_digit_cnt.append(cnt)
            cnt = 1
    
    repeat_digit_cnt.append(cnt)
    
    if 2 in repeat_digit_cnt:
        return True
    
    return False

def case2_check(num):

    str_num = str(num)
    for i in range(5):
        if int(str_num[i]) > int(str_num[i+1]):
            return False
    
    return True    

# PART 1

count = 0
for val in range(168630, 718099):
    if case1_check(val) and case2_check(val):
        count += 1

print(count)

# PART 2

count = 0
for val in range(168630, 718099):
    if case1_p2_check(val) and case2_check(val):
        count += 1
        
print(count)