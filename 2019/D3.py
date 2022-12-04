# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:19:38 2022

@author: sbharadwaj
"""
import math

def read_data(filename):
    
    with open(filename) as f:
        lines = f.readlines()
        
    input_list = [line.strip().split(',') for line in lines]
        
    return input_list

op_lst = read_data("D3.txt")

coords1 = set()
coords2= set()

def add_coords(op_lst, coords):
    x, y = (0, 0)
    for val in op_lst:
        direction = val[0]
        amt = int(val[1:])
        if direction == 'U':
            for _ in range(amt):
                y += 1
                coords.add((x, y))
        elif direction == 'D':
            for _ in range(amt):
                y -= 1
                coords.add((x, y))
        elif direction == 'L':
            for _ in range(amt):
                x -= 1
                coords.add((x, y))
        elif direction == 'R':
            for _ in range(amt):
                x += 1
                coords.add((x, y))
    
    return coords 

def manhattan(x, y):

    return abs(0-x) + abs(0-y)

coords1 = add_coords(op_lst[0], coords1)
coords2 = add_coords(op_lst[1], coords2)

def count_steps(op_lst, tx, ty):
    x, y = (0, 0)
    steps = 0
    for val in op_lst:
        direction = val[0]
        amt = int(val[1:])
        if direction == 'U':
            for _ in range(amt):
                y += 1
                steps += 1
                if x == tx and y == ty:
                    return steps
        elif direction == 'D':
            for _ in range(amt):
                y -= 1
                steps += 1
                if x == tx and y == ty:
                    return steps
        elif direction == 'L':
            for _ in range(amt):
                x -= 1
                steps += 1
                if x == tx and y == ty:
                    return steps
        elif direction == 'R':
            for _ in range(amt):
                x += 1
                steps += 1
                if x == tx and y == ty:
                    return steps
    

intsec = coords1.intersection(coords2)

shortest = math.inf
for x, y in intsec:
    dist = manhattan(x, y)
    if dist < shortest:
        shortest = dist

print(shortest)

min_steps = math.inf
for tx, ty in intsec:
    steps1 = count_steps(op_lst[0], tx, ty)
    steps2 = count_steps(op_lst[1], tx, ty)
    tot_steps = steps1 + steps2
    if tot_steps < min_steps:
        min_steps = tot_steps

print(min_steps)
    
