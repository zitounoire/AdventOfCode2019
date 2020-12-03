#!/usr/bin/python3

def bi_slide(right, skip):
    x = 0
    sum = 0
    for line in trail:
        if skip and trail.index(line) % 2 != 0:
            continue
        if line[x] == '#':
            sum +=1
        x += right
        if x > 30:
            x -= 31
    return sum

trail = [line.strip('\n') for line in open('input.txt','r').readlines()]

# day 1
print('Part 1: ', bi_slide(3,False))

# day 2
print('Part 2: ', bi_slide(1,False) * bi_slide(3,False) * bi_slide(5,False) * bi_slide(7,False) * bi_slide(1, True))