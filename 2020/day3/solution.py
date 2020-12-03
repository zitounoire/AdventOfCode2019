#!/usr/bin/python3
import numpy

def bi_slide(right, skip):
    x = sum =0
    for line in trail:
        if skip and trail.index(line) %2 != 0:
            continue
        if (line[x] == '#'):
            sum +=1
        x += right
        if x > 30:
            x -= 31 
    return sum

trail = [line.strip('\n') for line in open('input.txt','r').readlines()]

print('Part 1: ', bi_slide(3,False)) # part 1

print('Part 2: ', numpy.prod([bi_slide(i,bool(i==2)) for i in [1,2,3,5,7]])) # part 2